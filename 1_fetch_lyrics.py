# import packages
import lyricsgenius # genius API https://github.com/johnwmillr/LyricsGenius
import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
from helper.ChartHelper import ChartLyrics
import time

# find .env file for genius authentication
load_dotenv(find_dotenv())

# get authentication variables
CLIENT_ACCESS_TOKEN = os.environ.get("CLIENT_ACCESS_TOKEN")

def authenticate_to_genius_api(token=CLIENT_ACCESS_TOKEN):
    return lyricsgenius.Genius(token)

def fetch_lyrics(chart_data):
    lyrics_data = []

    # loop through all artists
    # authenticate to api
    counter = 0
    for index, row in chart_data.iterrows():
        title = row['title']
        artist = row['artist']

        genius = authenticate_to_genius_api()

        # search for track
        track = genius.search_song(title=title,
                                    artist=artist)

        # sanity check
        lyrics_instance = ChartLyrics(title, artist, track)

        lyrics_data.append(lyrics_instance.return_lyrics_instance())

        counter+=1

        if counter % 100 == 0:
            # safety copy
            overall_lyrics_pd = pd.DataFrame(lyrics_data)
            overall_lyrics_pd.columns = ChartLyrics.COLUMN_NAMES

            # export lyrics
            overall_lyrics_pd.to_csv('./data/Lyrics_2021.csv',
                                      sep=";",
                                      index=False)

            time.sleep(5) # avoid being kicked from API

    return lyrics_data

if __name__ == '__main__':

    chart_data = pd.read_csv('./data/Billboard_Charts_2021.csv', sep=";",
                             index_col=0)

    # drop duplicates since tracks do not have to be fetched several times
    chart_data = chart_data.drop_duplicates(subset=['artist', 'title'])
    print(chart_data.shape)

    # get lyrics data and transform to dataframe
    overall_lyrics = fetch_lyrics(chart_data=chart_data)





