# Lyrics 2021
Fetch Lyrics for 2021's Billboard Top 200 Tracks.

## 1. Billboard data
The lyrics at hand are all based on 2021's Billboard 200 [weekly charts](https://www.billboard.com/charts/billboard-200).
To download the chart data, the Python wrapper [billboard-charts](https://github.com/guoguo12/billboard-charts) is utilized.

## 2. Lyrics
The lyrics are fetched from [Genius' API](https://github.com/johnwmillr/LyricsGenius). To reproduce the code, a **CLIENT_ACCESS_TOKEN** is necessary.
Due to the sensitivity of the information, the variable is stored in an **.env** file.