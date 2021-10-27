import billboard
from datetime import datetime

import pandas as pd

from helper.ChartHelper import TrackInformation

FIRST_DATE = '2021-01-01'
LAST_DATE = '2021-10-23'

if __name__ == '__main__':
    overall_chart_data = []

    # make sure to only get the data for specific time frame
    while datetime.strptime(LAST_DATE, '%Y-%m-%d') >= datetime.strptime(FIRST_DATE, '%Y-%m-%d'):
        chart = billboard.ChartData('billboard-global-200', date=LAST_DATE)
        # process data
        chart_processed = [TrackInformation(x, LAST_DATE).return_track_array() for x in chart]

        # append to overall dataframe
        overall_chart_data.extend(chart_processed)

        LAST_DATE = chart.previousDate

    overall_chart_data = pd.DataFrame(overall_chart_data)
    overall_chart_data.columns = TrackInformation.COLUMN_NAMES

    # export to csv
    overall_chart_data.to_csv('./data/Billboard_Charts_2021.csv',
                              sep=";") # billboard global 200