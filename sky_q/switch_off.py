import requests
import json

# Set up your Sky Q box IP address and the MAC address
box_ip = "192.168.1.100"
mac_address = "AA:BB:CC:DD:EE:FF"

# Send the power off command to the Sky Q box
url = f"http://{box_ip}/sky/remote/power"
data = json.dumps({"mac": mac_address, "power": "standby"})
headers = {'Content-Type': 'application/json'}
response = requests.put(url, data=data, headers=headers)

# Check the response status
if response.status_code == 200:
    print("Sky Q box has been successfully switched off.")
else:
    print(f"Error: {response.status_code}")
