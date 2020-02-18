from data import config
import pandas as pd
import requests
import numpy as np


def check_auth(dest=config.ENDPOINT, headers=config.API_KEY):
    r = requests.get(dest + "/workspaces/", headers=headers)
    if r.status_code == 200:
        return r.status_code
    else:
        print(
            "possible authorisation issue, please check config:\n" + str(r.status_code)
        )
        return r.status_code


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

    times_expanded["minutes_waste"] = np.round(
        times_expanded.minutes / 60 * 4
    ) / 4 * 60 - (
        times_expanded.minutes
    )  ## track trimmed minutes ≠ve = round up

    return times_expanded


def check_min_date(df):
    return df["start"].min()


def status_trimmed(df):
    print("hours rounded total = " + str(times_trimcheck["hours_rounded"].sum()))
    print("sum minutes trimmed = " + str(times_trimcheck["minutes_waste"].sum()))


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
    )  # use copied row as index then drop it setting index
    df.index = pd.to_datetime(df.index)
    df.sort_values(by="startIndex", ascending=False)  # order in reverse
    return df


def filter_by_month(df, month):
    """filter a dataframe by month, where month is integer, and index is datetime"""
    month_df = df[df.index.month.isin([month])]
    return month_df


def sum_name_grouped(df):
    df = df.groupby("name").sum()
    return df
