import requests
import base64

def get_spotify_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to get token: {response.status_code}, {response.text}")

#print(get_spotify_token("9b3001e75c2346478a951e4bfefd8eff", "087ed2886e4b489091a9cd82b665c5fd"))

#base64 library:decode / encode