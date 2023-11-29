import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIiwidXNlcm5hbWUiOiJ1c2VyQGV4YW1wbGUuY29tIiwiaXNfbWFuYWdlciI6ZmFsc2V9.XBOEScQVZGuhqZcyi_8GibT79FAcOSmRpgYgYanZUEE"

# Use the obtained token to send a POST request to the /test endpoint
test_url = "http://localhost:8000/user/test"
headers = {"Authorization": f"Bearer {token}"}

# Make an authenticated POST request to the /test endpoint
response = requests.post(test_url, headers=headers)

# Print the response content
print(response.json())
