# Clockify Timesheet
Using the Clockify API with Python &amp; Requests to populate a timesheet.

## Installation
```
# Get the repo
git clone https://github.com/GeoJones/clockify-timesheet.git

# Create virtualenv & install packasges
mkvirtualenv clockify
pip install pip-tools
pip-sync

# Copy config_template.py to config.py and complete

# Run the following to find your user id
curl -H "content-type: application/json" -H "X-Api-Key: {YOUR_API_KEY}" -X GET https://api.clockify.me/api/v1/user

# Clockify config details
#   - API_KEY from https://clockify.me/user/settings -> at the bottom
#   - WORKSPACE_ID from https://clockify.me/workspaces -> Settings -> in URL
#   - USER_ID from above
```

## How to use
```
python -m pipeline.core
```


## Install virtualenv & virtualenvwrapper
```
# Install virtualenv
pip install virtualenv

# Install virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
pip install virtualenvwrapper
# Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs by adding following to .zshrc
zshconfig
#    # "Tell shell to source virtualenvwrapper.sh and where to put the virtualenvs"
#    export WORKON_HOME=$HOME/.virtualenvs
#    export PROJECT_HOME=$HOME/code
#    source /usr/local/bin/virtualenvwrapper.sh
source ~/.zshrc
source /usr/local/bin/virtualenvwrapper.sh
# Now let's make a virtualenv
mkvirtualenv venv
workon venv
# Commands `workon venv`, `deactivate`, `lsvirtualenv` and `rmvirtualenv` are useful
# WARNING: When you brew install formulae that provide Python bindings, you should not be in an active virtual environment.
# (https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md)
deactivate
```
