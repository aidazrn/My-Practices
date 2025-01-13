import requests
from get_token import get_spotify_token

def get_songs_by_singer(singer_name, token):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "q": singer_name,
        "type": "track",
        "limit": 10  # Limit the number of results
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        tracks = response.json().get("tracks", {}).get("items", [])
        return [track["name"] for track in tracks]
    else:
        raise Exception(f"Failed to fetch songs: {response.status_code}, {response.text}")
    
client_id = "9b3001e75c2346478a951e4bfefd8eff"
client_secret = "087ed2886e4b489091a9cd82b665c5fd"

token = get_spotify_token(client_id, client_secret)
print(get_songs_by_singer("eminem", token))