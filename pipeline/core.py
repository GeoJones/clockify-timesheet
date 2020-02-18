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

# PROJECT CONFIG

CLIENT = config.CLIENT

# PERSONAL CREDENTIALS
API_KEY = config.API_KEY

# API BAse Endpoint URLS (as string)
ENDPOINT = config.ENDPOINT

# Check All working okay
print(utils.check_auth())

print(endpoints.EP["ep_te"])


### LOAD PROJECTS FROM CLOCKIFY ###

r_pr = requests.get(endpoints.EP["ep_pr"], headers=API_KEY)
df_pr = pd.DataFrame(r_pr.json())
projects = df_pr
projects.head(2)

### LOAD TIME ENTRIES FROM CLOCKIFY ###

r_te = requests.get(endpoints.EP["ep_te"], headers=API_KEY)
df_time = pd.DataFrame(r_te.json())
times = df_time
times.head(2)

# # Expand Time Interval

times = utils.expand_time(times)

# print the earliest date to check how far back data goes
print(utils.check_min_date(times))

#

df = utils.merge_times_proj(times, projects)

# Filter by clientName as set in config: CLIENT

df = utils.filter_by_clientName(df)

# set the index as start date/time, then order the dataframe

df = utils.date_index_order(df)


# filter by Month

df = utils.filter_by_month(df, month=12)  # for february example

""" # irrelevant - example of resampling
week_total = df.resample("W").sum()
day_total = df.resample("B") """

# Example: Group by Business Day and 'name'

df_grouped_daily = df.groupby([pd.Grouper(freq="B"), "name"])

print(df_grouped_daily.sum())

print(utils.sum_name_grouped(df))
