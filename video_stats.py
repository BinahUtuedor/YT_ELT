import requests
import json

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "MrBeast"

def get_palylist_id():
        
    try:
    
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(url)

        response.raise_for_status()   # Raises error for 4xx and 5xx responses

        data = response.json()

        # print(json.dumps(data,indent=4))

        channel_items = data["items"][0]

        channel_palylistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        # print(channel_palylistId)

        return channel_palylistId 

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    get_palylist_id()
