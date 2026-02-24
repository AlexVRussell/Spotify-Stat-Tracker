import os
import base64
from dotenv import main
import webbrowser
from requests import post
import sqlite3
import requests
from flask import Flask, request
from threading import Thread
from queue import Queue

main.load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

auth_code_queue = Queue()
app = Flask(__name__)


# Open Spotify authorization URL in the browser
# Prompts user to log into Spotify
def get_authorization_code():
    auth_url = (
        "https://accounts.spotify.com/authorize"
        "?response_type=code"
        f"&client_id={client_id}"
        "&scope=user-read-recently-played"
        "&redirect_uri=http://127.0.0.1:8888/callback"
        "&show_dialog=true"
    )
    webbrowser.open(auth_url)

def get_token(auth_code):
    token_url = "https://accounts.spotify.com/api/token"
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = base64.b64encode(auth_string.encode("utf-8"))
    headers = {
        "Authorization": f"Basic {auth_bytes.decode('utf-8')}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": "http://127.0.0.1:8888/callback"
    }
    response = post(token_url, headers=headers, data=data)
    return response.json()

def fetch_recently_played(access_token):
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=50"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def create_tables():
    conn = sqlite3.connect("stats.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS plays (
                    track_id TEXT,
                    name TEXT,
                    artist TEXT,
                    album TEXT,
                    played_at TEXT UNIQUE,
                    duration REAL,
                    PRIMARY KEY (track_id, played_at)
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS artists (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    popularity INTEGER
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS albums (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    artist TEXT,
                    release_date TEXT
                )''')

    conn.commit()
    conn.close()

def store_tracks(tracks):
    conn = sqlite3.connect("stats.db")
    c = conn.cursor()

    for item in tracks['items']:
        track = item['track']
        played_at = item['played_at']
        duration_ms = track['duration_ms']

        if duration_ms < 30000:
            continue

        duration_min = duration_ms // 60000

        c.execute('''SELECT 1 FROM plays WHERE track_id = ? AND played_at = ?''', (track['id'], played_at))
        exists = c.fetchone()

        if not exists:
            c.execute('''INSERT INTO plays (track_id, name, artist, album, played_at, duration) 
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (track['id'], track['name'], track['artists'][0]['name'],
                       track['album']['name'], played_at, duration_min))
        else:
            # Print the tracks that in that call have already been stored in the database
            print(f"Track already exists in database: {track['name']} at {played_at} Duration - {duration_min:.2f} minutes")

    conn.commit()
    conn.close()

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')
    auth_code_queue.put(authorization_code)
    return "Authorization code received successfully."

def start_flask():
    app.run(port=8888)


def main():
    create_tables()
    flask_thread = Thread(target=start_flask)
    flask_thread.start()
    get_authorization_code()

    # Wait for authorization code from Flask callback
    authorization_code = auth_code_queue.get()

    # Exchange authorization code for tokens
    tokens = get_token(authorization_code)
    access_token = tokens["access_token"]

    recently_played = fetch_recently_played(access_token)
    store_tracks(recently_played)
    print("Data has been successfully stored in the database.")


if __name__ == "__main__":
    main()
