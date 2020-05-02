""" Use this list to define which headers are dropped during drop_headers() function"""

drop_filter = {
    "id_timeEntry": "True",
    "description": "True",
    "tagIds": "False",
    "userId": "False",
    "billable_timeEntry": "True",
    "taskId": "False",  # Potentially very useful
    "projectId": "False",  # obtained from the join
    "timeInterval": "False",  # may nee to drop this as part of the unzipping
    "workspaceId_timeEntry": "False",  # assumed irrelevant
    "isLocked": "False",  # premium feature
    "customFieldValues": "False",  # premium feature
    "start": "True",  #
    "end": "True",
    "duration_timeEntry": "False",  # e.g. 2020-04-16 15:38:05+00:00    PT27M29S
    "minutes": "True",
    "hours_rounded": "True",
    "minutes_rounded_up": "True",
    "id_proj": "False",
    "name": "True",
    "hourlyRate": "False",  ## BUILT IN ## Should use
    "clientId": "False",  # could be more accurate, might be more fixed if name changes
    "workspaceId_proj": "False",  # e.g. 5c+6984%b079&73a56e892cb
    "billable_proj": "True",
    "memberships": "True",  ## invesgibate this
    "color": "True",
    "estimate": "False",  # projected time for task
    "archived": "False",
    "duration_proj": "False",
    "clientName": "True",
    "note": "False",
    "template": "False",
    "public": "False",
    "_merge": "True",  # check all True? from proj-time merge
}

