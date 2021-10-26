# import packages
import lyricsgenius # genius API https://github.com/johnwmillr/LyricsGenius
import os
from dotenv import load_dotenv, find_dotenv
import pandas as pd
from helper.ChartHelper import ChartLyrics

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
    for index, row in chart_data.iterrows():
        genius = authenticate_to_genius_api()

        title = row['title']
        artist = row['artist']

        # search for track
        track = genius.search_song(title=title,
                                   artist=artist)

        # sanity check
        lyrics_instance = ChartLyrics(title, artist, track)

        lyrics_data.append(lyrics_instance.return_lyrics_instance())

    return lyrics_data

if __name__ == '__main__':

    chart_data = pd.read_csv('./data/Billboard_Charts_2021.csv', sep=";",
                             index_col=0)

    # drop duplicates since tracks do not have to be fetched several times
    chart_data = chart_data.drop_duplicates(subset=['artist', 'title'])

    # get lyrics data and transform to dataframe
    overall_lyrics = fetch_lyrics(chart_data=chart_data)
    overall_lyrics = pd.DataFrame(overall_lyrics)
    overall_lyrics.columns = ChartLyrics.COLUMN_NAMES

    # export lyrics
    overall_lyrics.to_csv('./data/Lyrics_2021.csv',
                          sep=";",
                          index=False)




