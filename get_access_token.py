import requests
import base64
import config

# Replace these with your actual API Client ID and API Client Secret
client_id = config.finra_api_client
client_secret = config.finra_api_secret

# Encode the client ID and client secret
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# FIP endpoint for generating access token
token_url = "https://ews.fip.finra.org/fip/rest/ews/oauth2/access_token?grant_type=client_credentials"

# Headers for the token request
headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Make the POST request to get the access token
response = requests.post(token_url, headers=headers)

if response.status_code == 200:
    access_token = response.json().get("access_token")
    print(f"Access Token: {access_token}")
    config.finra_access_token = access_token
    # Save the access token to a text file just in case 
    with open("access_token.txt", "w") as file:
        file.write(access_token)
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}")
    print(response.text)