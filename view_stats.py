import sqlite3

# Function to view top 10 tracks ordered by total minutes listened since June 16th, 2024 (Using the last duplicate track date)
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

    print("Top Tracks by Total Minutes Listened:\n")
    for row in rows:
        track_id, name, artist, album, total_minutes = row
        print(f"Track: {name}, Artist: {artist}, Album: {album}, Total Minutes: {total_minutes}")

    conn.close()

'''
The view_artists adn view_albums functions are not yet implemented, I am not sure how I am going to calculate the total 
number of minutes for these categories
'''

# Function to view top artists ordered by popularity
def view_artists():
    conn = sqlite3.connect("stats.db")
    c = conn.cursor()

    c.execute("SELECT * FROM artists ORDER BY popularity DESC LIMIT 10")
    rows = c.fetchall()

    print("Top Artists:")
    for row in rows:
        print(row)

    conn.close()

# Function to view top albums ordered by release date
def view_albums():
    conn = sqlite3.connect("stats.db")
    c = conn.cursor()

    c.execute("SELECT * FROM albums ORDER BY release_date DESC LIMIT 10")
    rows = c.fetchall()

    print("Top Albums:")
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    view_tracks()
    print()
    view_artists()
    print()
    view_albums()
