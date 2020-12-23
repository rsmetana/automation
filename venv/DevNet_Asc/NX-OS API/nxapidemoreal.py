import requests
import json

switchuser = 'cisco'
switchpassword ='cisco'

url = 'https://172.16.1.68/ins'
myheader = {'content-type':'application/json'}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": "show cdp nei",
        "output_format": "json"
    }
}

response = requests.post(url, data=json.dumps(payload),headers=myheader, auth=(switchuser,switchpassword),verify=False).json()
print(response)