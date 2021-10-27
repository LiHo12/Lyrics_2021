import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
from PIL import Image

ENGLISH_STOPWORDS = stopwords.words('english')
# extend ENGLISH_STOPWORDS with common words
ENGLISH_STOPWORDS.extend(['im', 'yeah', 'like', 'dont', 'know', 'get', 'got',
                          'oh', 'aint', 'cant', 'caus', 'en', 'caus', 'ill',
                          'ft', 'ooh', 'remix', 'gon', 'even', 'that',
                          'uh', 'would', 'make', 'se', 'til', 'ive', 'everyth',
                          'tryna', 'e', 'em', 'that', 'your', 'could',
                          'la', 'gotta', 'said', 'goin', 'gone', 'le', 'ya',
                         'gonna', 'huh', 'eh', 'id', 'ima'])
PORTER_STEMMER = PorterStemmer()

def cleanse_lyrics(data):
    # cleanse lyrics column
    # lower case stuff
    data['lyrics'] = data['lyrics'].str.lower()

    # replace EmbedShare, urlcopyembedcopy
    # replace special connotations from Genius
    # remove all [], they indicate all special parts in a track
    # remove all punctuations
    data['lyrics'] = data['lyrics'].str.replace(r'\[.*\]|embedshare|urlcopyembedcopy|[^\w\s]', '')

    # replace all parts with more than one whitespace
    data['lyrics'] = data['lyrics'].str.replace(r'\s{2,}', ' ')

    # tokenize words in lyrics
   # remove all stop words
    data['lyrics'] = data['lyrics'].apply(lambda x: [item for item in str(x).split() if str(item) not in ENGLISH_STOPWORDS])

    # stem all words
    data['lyrics'] = data['lyrics'].apply(lambda x: [PORTER_STEMMER.stem(word) for word in x])

    # remove all stop words
    data['lyrics'] = [' '.join(x) for x in data['lyrics']]

    data['lyrics'] = data['lyrics'].apply(lambda x: [item for item in str(x).split() if str(item) not in ENGLISH_STOPWORDS])
    return data

def print_wordcloud(data):
    overall_lyrics = []
    for lyrics in data['lyrics']:
        overall_lyrics.extend(lyrics)
    # get counter
    counter = Counter(overall_lyrics)

    # vectorize image
    music_mask = np.array(Image.open('music_pc.jpg'))
    colors = ImageColorGenerator(music_mask)
    wc = WordCloud(background_color='white',
                   max_words=500,
                   mask = music_mask,
                   width=music_mask.shape[1],
                   height=music_mask.shape[0],
                   color_func=colors)
    wc.generate_from_frequencies(counter)

    plt.figure(figsize=(17,10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    # save figure
    plt.savefig('Overall_Wordcloud.png')

if __name__ == "__main__":

    # read data
    data = pd.read_csv('Lyrics_2021.csv',
                       sep=";",
                       index_col=0)

    # cleanse data
    data = cleanse_lyrics(data)

    print_wordcloud(data=data)
