#!/usr/bin/env python3
​
import netmiko
import csv
import pandas as pd
​
​
def parse_wlan(wlan_list):
    wlans = []
    for line in wlan_list[2:]:
        split_line = line.split()
        wlan_dict = {}
        if len(split_line) != 0:
            wlan_dict["wlan_id"] = split_line[0]
            wlan_dict["interface"] = split_line[1]
            wlan_dict["nac"] = split_line[2]
            wlan_dict["rp"] = split_line[3]
            wlan_dict["dns_profile"] = split_line[4]
            wlans.append(wlan_dict)
​
    return wlans
​
​
def ap_groups(ip_addr):
    cisco_wlc = {
        "device_type": "cisco_wlc",
        "ip": ip_addr,
        "username": "admin",
        "password": "%tech^privS",
    }
    header = ["AP_Group", "2.4 GHz RF Profile", "5 GHz RF Profile"]
    net_connect = netmiko.ConnectHandler(**cisco_wlc)
    cmd = "show wlan apgroups"
    output = net_connect.send_command(cmd)
    lines = output.splitlines()
​
    site_wlan_dict = {}
    wlan_objs = []
    wlan_flag = False
    for line in lines:
        if line.startswith("Site Name"):
            temp_site = line[50:]
        if line.startswith("WLAN ID"):
            wlan_flag = True
        elif line.startswith("*"):
            wlan_flag = False
            site_wlan_dict[temp_site] = wlan_objs
            wlan_objs = []
        if wlan_flag:
            wlan_objs.append(line)
​
    for key in site_wlan_dict:
        site_wlan_dict[key] = parse_wlan(site_wlan_dict[key])
​
    apg = []
    bob = "\n".join(
        line
        for line in output.splitlines()
        if any(
            line.startswith(word)
            for word in ("Site Name", "2.4 GHz band", "5 GHz band")
        )
    )
    print("---------------")
    bobo = bob.splitlines()
    for line in bobo:
        mylist = line[50:]
        # print(line[50:])
        print(mylist)
        apg.append(mylist)
    print("---------------")
    sites = apg[::3]
    two_four_ghz = apg[1::3]
    five_ghz = apg[2::3]
​
    df1 = pd.DataFrame(sites, columns=["AP Group Name"])
    df2 = pd.DataFrame(two_four_ghz, columns=["2.4 GHz RF Profile"])
    df3 = pd.DataFrame(five_ghz, columns=["5 GHz RF Profile"])
    rows = []
    for key in site_wlan_dict:
        site_name = key
        data_row = site_wlan_dict[key]
        row_tup = ()
        for nest in data_row:
            temp = [site_name]
            for row in nest:
                temp.append(nest[row])
            row_tup = tuple(temp)
            rows.append(row_tup)
​
    df4 = pd.DataFrame(
        rows,
        columns=[
            "AP Group Name",
            "WLAN ID",
            "INTERFACE",
            "NAC",
            "RP",
            "DNS PROFILE",
        ],
    )
​
    frames = [df1, df2, df3]
    df = pd.concat([df1, df2, df3], axis=1)
    df = pd.merge(df, df4, how="left", on="AP Group Name")
    df.to_csv(f"RF_Profiles_{ip_addr}.csv", index=False)
​
​
if __name__ == "__main__":
    ip_list = ["10.160.0.7"]
    for ip in ip_list:
        profiles = ap_groups(ip)