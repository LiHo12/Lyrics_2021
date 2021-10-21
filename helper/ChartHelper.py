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