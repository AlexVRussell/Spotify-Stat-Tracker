# Spotify-Stat-Tracker

This project is a Spotify stat tracker that fetches your recently played tracks and stores them in an SQLite database using the Spotify Web API. 

Takes the authorization code from the Spotify authoraztion url and input. Run view_stats.py to see in the console or terminal your top ten songs on spotify ordered by minutes!

Important to create a .env file and put in your own CLIENT_ID and CLIENT_SECRET from the Spotify for Developers Dashboard.

*Improvements*

- Implement view_artists and view_albums functions to calculate total minutes listened for these categories. (In progress)

- Automate the authorization code fetching process.

- Figure out why the authorization code needs to be inputed twice (run the code 2 seperate times) to fetch the most recent data

- Schedule the script to run at regular intervals to keep the database updated.

If you have any improvements to this project, please reach out. This is my first time working with APIs so I'd love to enhance the code and learn new things. Thanks!
