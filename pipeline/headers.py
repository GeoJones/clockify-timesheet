drop_list = {}
""" for a in [
    "id_timeEntry",
    "description",
    "tagIds",
    "userId",
    "billable_timeEntry",
    "taskId",
    "projectId",
    "timeInterval",
    "workspaceId_timeEntry",
    "isLocked",
    "customFieldValues",
    "start",
    "end",
    "duration_timeEntry",
    "minutes",
    "hours_rounded",
    "minutes_rounded_up",
    "id_proj",
    "name",
    "hourlyRate",
    "clientId",
    "workspaceId_proj",
    "billable_proj",
    "memberships",
    "color",
    "estimate",
    "archived",
    "duration_proj",
    "clientName",
    "note",
    "template",
    "public",
    "_merge",
]:
    drop_list.update({a: "True"}) """

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

