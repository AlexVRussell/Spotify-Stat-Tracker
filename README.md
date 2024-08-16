# Spotify-Stat-Tracker

This project is a Spotify stat tracker that fetches your recently played tracks and stores them in an SQLite database using the Spotify Web API. 

Takes the authorization code from the Spotify authoraztion url and input. Run view_stats.py to see in the console or terminal your top ten songs on spotify ordered by minutes!

Important to create a .env file and put in your own CLIENT_ID and CLIENT_SECRET from the Spotify for Developers Dashboard.

Disclaimer, there is no direct endpoint in Spotify's API for minutes or streams. So the minutes may be off by some decimal points, but after looking into majority of the songs I most listen to the duration is very accurate.

*Improvements*

- Implement view_artists and view_albums functions to calculate total minutes listened for these categories. (In progress)

- Figure out why the main script sometimes needs to be ran twice to fetch the most recent data (This only ever happens really in my testing when code is ran alot in a period of time)

- Schedule the script to run at regular intervals to keep the database updated. (Might do windows task scheduling, if so I will upload a video of how to set it up here)

If you have any improvements to this project, please reach out. This is my first time working with APIs so I'd love to enhance the code and learn new things. Thanks!
