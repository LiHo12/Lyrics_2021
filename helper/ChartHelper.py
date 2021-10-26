class TrackInformation:
    COLUMN_NAMES = ['title', 'artist', 'rank', 'weeks', 'current_week']

    def __init__(self, ChartEntry,
                 current_week):
        self.title = ChartEntry.title
        self.artist = ChartEntry.artist
        self.rank = ChartEntry.rank
        self.weeks = ChartEntry.weeks
        self.current_week = current_week

    def return_track_array(self):
        return [self.title,
                self.artist,
                self.rank,
                self.weeks,
                self.current_week]


class ChartLyrics:
    COLUMN_NAMES = ['title', 'artist', 'lyrics', 'pageviews', 'url']

    def __init__(self, title, artist, track):
        self.title = title
        self.artist = artist
        self.lyrics = None
        if hasattr(track, 'lyrics'):
            self.lyrics = track.lyrics
        self.pageviews = None
        if hasattr(track, 'stats.pageviews'):
            self.pageviews = track.stats.pageviews
        self.url = None
        if hasattr(track, 'song_art_image_url'):
            self.url = track.song_art_image_url

    def return_lyrics_instance(self):
        return [self.title,
                self.artist,
                self.lyrics,
                self.pageviews,
                self.url]