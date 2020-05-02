from data import config
from pipeline import headers
import pandas as pd
import requests
import numpy as np
import datetime as dt


def check_auth(dest=config.ENDPOINT, headers=config.API_KEY):
    r = requests.get(dest + "/workspaces/", headers=headers)
    if r.status_code == 200:
        return r.status_code
    else:
        print(
            "possible authorisation issue, please check config:\n" + str(r.status_code)
        )
        return r.status_code


# should use try above>?

""" r = requests.get(ENDPOINT, headers=HEADER)
r_ws = requests.get(ep_ws, headers=HEADER)
r_te = requests.get(ep_te, headers=HEADER)
r_pr = requests.get(ep_pr, headers=HEADER) """


def expand_time(times):
    # function to create a new df with the times expanded out and hours rounded
    times_expanded = times
    times_expanded["start"] = times_expanded["timeInterval"].apply(
        lambda x: pd.to_datetime(x["start"])
    )
    times_expanded["end"] = times_expanded["timeInterval"].apply(
        lambda x: pd.to_datetime(x["end"])
    )
    times_expanded["duration"] = times_expanded["timeInterval"].apply(
        lambda x: (x["duration"])
    )

    times_expanded["minutes"] = (times_expanded.end - times_expanded.start).apply(
        lambda x: x.seconds / 60
    )

    times_expanded["hours_rounded"] = (
        np.round(times_expanded.minutes / 60 * 4) / 4
    )  ## rounded hours

    times_expanded["minutes_rounded_up"] = np.round(
        times_expanded.minutes / 60 * 4
    ) / 4 * 60 - (
        times_expanded.minutes
    )  ## track trimmed minutes ≠ve = round up

    return times_expanded


def check_min_date(df):
    return df["start"].min()


def status_trimmed(df):
    print("hours rounded total = " + str(times_trimcheck["hours_rounded"].sum()))
    print(
        "sum minutes rounded up = " + str(times_trimcheck["minutes_rounded_up"].sum())
    )


def merge_times_proj(left, right):
    merged = pd.merge(
        left,  # should be times
        right,  # should be projects
        how="left",
        left_on="projectId",
        right_on="id",
        left_index=False,
        right_index=False,
        sort=True,
        suffixes=("_timeEntry", "_proj"),
        copy=True,
        indicator=True,
        validate="m:1",
    )
    return merged


def filter_by_clientName(df):
    filtered = df[df["clientName"] == config.CLIENT]
    return filtered


def date_index_order(df):
    df["startIndex"] = df["start"]  # copy start date
    df = df.set_index(
        "startIndex", drop=True, verify_integrity=True
    )  # use copied column as index then drop it setting index
    df.index = pd.to_datetime(df.index)
    df.sort_values(by="startIndex", ascending=False)  # order in reverse
    return df


def filter_year_month(df, year=0, month=0):
    """filter a dataframe by year/month, where value is integer, and index is datetime, default to now()"""

    if year == 0:
        df = df[df.index.year.isin([(dt.datetime.now().year)])]
    elif year == "all":
        df = df  # 'all' parameter skips
    else:
        df = df[df.index.year.isin([year])]

    if month == 0:
        df = df[df.index.month.isin([(dt.datetime.now().month)])]
    elif month == "all":
        df = df  # 'all' parameter skips
    else:
        df = df[df.index.month.isin([month])]

    return df


def sum_name_grouped(df):
    df = df.groupby("name").sum()
    return df


def NaN_filter(df, name=True):
    """ Filter out NaN values as required, default, ["name"] NaN changed to 'No Project' """
    df["name"].fillna("No Project", inplace=True)
    df["clientName"].fillna("No Client", inplace=True)
    return df


def drop_headers(df):
    to_drop = []
    dict_to_drop_now = {}
    for x in df.columns.tolist():
        if headers.drop_filter[x] == "False":
            to_drop.append(x)
        else:
            continue
    print("Dropping:\n" + str(to_drop))
    df.drop(to_drop, axis=1, inplace=True)
    print("Dropped")
    return df
