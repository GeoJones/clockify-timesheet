import requests
import numpy as np
from pandas.io.json import json_normalize
import pandas as pd
import os
from pathlib import Path

CLOCK_CACHE = Path("./data/clock_cache/")
CACHE_FILE = Path("./data/clock_cache/cache.pkl")

from data import config
from pipeline import utils
from pipeline import endpoints
from pipeline import collect

from joblib import Memory

cachedir = "./data"
memory = Memory(cachedir, verbose=1)

# From PROJECT *CONFIG*

CLIENT = config.CLIENT

# PERSONAL CREDENTIALS
API_KEY = config.API_KEY

# API BAse Endpoint URLS (as string)
ENDPOINT = config.ENDPOINT


# @memory.cache  # (ignore=[])  # nothing to ignore
def collect(pickle=False):
    if pickle == True:
        clock_cache_file = Path("./data/pkl/cache.pkl")
        if clock_cache_file.is_file():
            df = pd.read_pickle("./data/pkl/cache.pkl")  #### NEED TO ADD EXPIRY HERE
            return df
        else:
            return collect(pickle=False)
    else:
        ### LOAD *PROJECTS* FROM CLOCKIFY ###

        r_pr = requests.get(endpoints.EP["ep_pr"], headers=API_KEY)
        df_pr = pd.DataFrame(r_pr.json())
        projects = df_pr
        projects.head(2)

        ### LOAD *TIMES* ENTRIES FROM CLOCKIFY ###

        r_te = requests.get(endpoints.EP["ep_te"], headers=API_KEY)
        df_time = pd.DataFrame(r_te.json())
        times = df_time
        times.head(2)

        # # Expand Time Interval in times

        times = utils.expand_time(times)

        # print the earliest date to check how far back data goes
        print(
            "The oldest entry starts on: \n" + str(utils.check_min_date(times)) + "\n"
        )

        df = utils.merge_times_proj(times, projects)

        # hard CACHE
        dump_loc = Path("./data/pkl/cache.pkl")
        df.to_pickle(dump_loc)

        return df
