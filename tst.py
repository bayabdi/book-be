import requests

manager_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIiwidXNlcm5hbWUiOiJ1c2VyQGV4YW1wbGUuY29tIiwiaXNfbWFuYWdlciI6dHJ1ZX0.jvLjNhNQnSpUiNFStWFbrtEuLOoRXZCIfHs_7UiGL9c"
user_token =    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsInVzZXJuYW1lIjoidXNlcjFAZXhhbXBsZS5jb20iLCJpc19tYW5hZ2VyIjpmYWxzZX0.EkOPwx_kWVbgmJauXnI9HAuvJDowy5cjcTahFzt6n44"
# Use the obtained token to send a POST request to the /test endpoint
test_url = "http://localhost:8000/appointment/list_by_status?status=1"
headers = {"Authorization": f"Bearer {manager_token}"}

# Make an authenticated POST request to the /test endpoint
response = requests.get(test_url, headers=headers)

# Print the response content
print(response.json())
