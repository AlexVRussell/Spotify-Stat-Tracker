import sqlite3
from datetime import datetime

timeUpdated = datetime.now()

counter = 0

# Function to view top 10 tracks ordered by total minutes listened since June 16th, 2024 (last duplicate track date)
# Figured out how to prompt users now lol. So DB is updated up until January 19th 2025, so it will be inaccurate.
def view_tracks():
    conn = sqlite3.connect("stats.db")
    c = conn.cursor()

    c.execute("""
        SELECT track_id, name, artist, album, SUM(duration) AS total_minutes 
        FROM plays 
        GROUP BY track_id, name, artist, album 
        ORDER BY total_minutes DESC 
        LIMIT 10
    """)
    rows = c.fetchall()

    print("Top Tracks Updated: " + timeUpdated.strftime("%B %d, %Y at %H:%M:%S"))
    print("Top Tracks by Total Minutes Listened:\n")

    for row in rows:
        track_id, name, artist, album, total_minutes = row

        print(f"Track: {name} | Artist: {artist} | Album: {album} | Total Minutes: {total_minutes:.2f}")

    # Easier way to read top 10 songs, but less info about the songs
    print("Top Tracks Updated: " + timeUpdated.strftime("%B %d, %Y at %H:%M:%S"))
    print("Top Tracks by Total Minutes Listened:\n")

    # Used for easy comparison for last update (Debugging)
    print("")
    for row in rows:
        track_id, name, artist, album, total_minutes = row

        print(f"{name:} - {total_minutes:.2f}")

    conn.close()


'''
The view_artists adn view_albums functions are not yet implemented, still working on how to calculate the total 
number of minutes for these categories
'''

if __name__ == "__main__":
    view_tracks()
