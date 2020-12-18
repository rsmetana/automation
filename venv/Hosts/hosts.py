import csv
import sys
with open('iplist.csv') as data:
    ip_list = csv.reader(data)
    for row in ip_list:
        site = row[0]
        ip = row[1]
        print(f"[{site.lower().strip()}_router]")
        print(f"{ip.strip()}")
        print(f"[{site.lower().strip()}_switches]")
        print(f"{ip[:-1]}[2:254]")
