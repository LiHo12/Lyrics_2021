# import packages
import lyricsgenius # genius API https://github.com/johnwmillr/LyricsGenius
import os
from dotenv import load_dotenv, find_dotenv

# find .env file for genius authentication
load_dotenv(find_dotenv())

# get authentication variables
# GENIUS_CLIENT_ID  = os.environ.get("GENIUS_CLIENT_ID")
# CLIENT_SECRET  = os.environ.get("CLIENT_SECRET")
CLIENT_ACCESS_TOKEN  = os.environ.get("CLIENT_ACCESS_TOKEN")

def authenticate_to_genius_api(token=CLIENT_ACCESS_TOKEN):
    return lyricsgenius.Genius(token)

if __name__ == '__main__':
    # authenticate to api
    genius = authenticate_to_genius_api()

    # search for track
    track = genius.search_song(title="Easy On Me",
                               artist="Adele")
    # get lyrics
    lyrics = track.to_text()

    # get stats
    pageviews = track.stats.pageviews
    # url
    url = track.song_art_image_url
    print(url)


    # TODO: integrate lyrics for all tracks
    # TODO: analyze lyrics