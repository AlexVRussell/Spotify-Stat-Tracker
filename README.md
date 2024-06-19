# Spotify-Stat-Tracker

This project is a Spotify stat tracker that fetches your recently played tracks and stores them in an SQLite database using the Spotify Web API.

*Project Objective*
The objective of this project is to track your Spotify listening habits by fetching recently played tracks and storing them in a local database. The data can then be analyzed to display top tracks, artists, and albums.

*Features*
Fetches recently played tracks from your Spotify account.
Stores track information in an SQLite database and orders by total minutes listened.
Provides views to see top tracks, artists, and albums.
Dependencies
Python 3.x
All libraries needed are imported in my code

*Improvements*
Implement view_artists and view_albums functions to calculate total minutes listened for these categories. (STILL WORKING ON IT)
Automate the authorization code fetching process using Flask.
Figure out why the authorization code needs to be imputed twice (run the code 2 seperate times) to fetch the most recent data
Schedule the script to run at regular intervals to keep the database updated.

If you have any improvements to this project, please reach out. This is my first time working with APIs so I'd love to enhance the code and learn new things. Thanks!
