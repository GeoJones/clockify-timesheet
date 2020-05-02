#!/usr/bin/env python
# coding: utf-8

import requests
import numpy as np
from pandas.io.json import json_normalize
import pandas as pd

# import seaborn as sns

from data import config
from pipeline import utils
from pipeline import endpoints
from pipeline import collect
from pipeline import headers


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


print(f"{bcolors.UNDERLINE}START{bcolors.ENDC}" + " ")
# Check All working okay
# print(utils.check_auth())  # should be 200

# print(endpoints.EP["ep_te"])


print(f"{bcolors.BOLD}COLLECT DATA{bcolors.ENDC}" + " ")
df = collect.collect(pickle=True)

# Filter by clientName as set in config: CLIENT
# df = utils.filter_by_clientName(df)

# Filter out NaNs (else are exluded in summary by Name or Client)
df = utils.NaN_filter(df)
df = utils.drop_headers(df)

# set the index as start date/time, then order the dataframe
df = utils.date_index_order(df)

print(f"{bcolors.OKGREEN}LIST OF HEADERS\n\n{bcolors.ENDC}" + " ")
print(df.columns.tolist())

print(f"{bcolors.WARNING}PREPARE TO FILTER{bcolors.ENDC}" + " ")
# filter by Month
df = utils.filter_year_month(df, month=4, year=0)  # for february example month = 2
print(f"{bcolors.OKBLUE}FILTER{bcolors.ENDC}" + " ")
print(df.head(2))


""" # irrelevant - example of resampling
week_total = df.resample("W").sum()
day_total = df.resample("B") """

# Example: Group by Business Day and 'name'

print(f"{bcolors.OKBLUE}groupby Day\n\n\n{bcolors.ENDC}" + " ")
df_grouped_daily = df.groupby([pd.Grouper(freq="B"), "name"])

print(utils.check_min_date(df))


print(df_grouped_daily.sum())
print(utils.sum_name_grouped(df))

