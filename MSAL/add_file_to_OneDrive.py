import json
import os
import msal
from msal.errors import TokenAcquisitionError
import requests

# Configuration
client_id = 'your_client_id'
client_secret = 'your_client_secret'
tenant_id = 'your_tenant_id'
scopes = ['https://graph.microsoft.com/Files.ReadWrite.All']
authority = "https://login.microsoftonline.com/" + tenant_id

# File to upload
file_path = 'path/to/file.txt'
file_name = os.path.basename(file_path)

# Build the MSAL app
app = msal.ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority
)

# Get an access token for the OneDrive API
try:
    result = app.acquire_token_for_client(scopes)
    access_token = result['access_token']
except TokenAcquisitionError as e:
    print("Error while acquiring access token: " + e)

# Build the OneDrive API request
url = 'https://graph.microsoft.com/v1.0/me/drive/root:/' + file_name + ':/content'
headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/octet-stream'}
data = open(file_path, 'rb').read()

# Send the request to upload the file
response = requests.put(url, headers=headers, data=data)

# Print the response
print(response.status_code)
print(response.json())
