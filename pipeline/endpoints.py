from data import config

EP = {
    "ep_te": str(
        config.ENDPOINT
        + "/workspaces/"
        + config.WORKSPACE_ID
        + str("/user/")
        + config.USER_ID
        + "/time-entries?page-size=1000"  # will need support for pagination
    ),
    "ep_ws": str(config.ENDPOINT + "/workspaces"),
    "ep_pr": str(config.ENDPOINT + "/workspaces/" + config.WORKSPACE_ID + "/projects?"),
}

