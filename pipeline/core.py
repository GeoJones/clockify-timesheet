"""
Usage:
    python -m pipeline.core
"""

import pandas as pd
from loguru import logger as log

from pipeline import collect, endpoints, utils

DEBUG = True


def main():
    # Check all working okay
    status_code = utils.check_auth()
    if status_code != 200:
        log.error(f"Connecting to Clockify API returned HTTP error code {status_code}")
        return

    if DEBUG:
        # Check endpoint
        log.debug(endpoints.EP["ep_te"])

    print("Collecting data")
    df = collect.collect(pickle=True)

    # Filter by clientName as set in config: CLIENT
    # df = utils.filter_by_clientName(df)

    # Filter out NaNs (else are exluded in summary by Name or Client)
    df = utils.NaN_filter(df)
    df = utils.drop_headers(df)

    # set the index as start date/time, then order the dataframe
    df = utils.date_index_order(df)

    print(f"List of headers: {df.columns.tolist()}")
    print(f"Prepare to filter")
    # Filter by Month
    df = utils.filter_year_month(df, month=4, year=0)  # for february example month = 2

    # # irrelevant - example of resampling
    # week_total = df.resample("W").sum()
    # day_total = df.resample("B")

    # Example: Group by Business Day and 'name'
    print(f"groupby Day")
    df_grouped_daily = df.groupby([pd.Grouper(freq="B"), "name"])

    print(utils.check_min_date(df))
    print(df_grouped_daily.sum())
    print(utils.sum_name_grouped(df))


if __name__ == "__main__":
    main()
