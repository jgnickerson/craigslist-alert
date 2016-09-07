import os

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

# What Craigslist subdirectories to search on.
# For instance, https://sfbay.craigslist.org/eby/ is the East Bay, and https://sfbay.craigslist.org/sfc/ is San Francisco.
# You only need the last three letters of the URLs.
AREAS = ["sfc"]


## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.

#CRAIGSLIST_HOUSING_SECTION = 'zip'

FURNITURE_QUERIES = [
    {"section": "zip", "query":"desk*", "slack_channel":"desks", "min_price": None, "max_price": None},
    {"section": "fua", "query":"desk*", "slack_channel":"desks", "min_price": None, "max_price": 100},
    {"section": "zip", "query":"dresser", "slack_channel":"dressers", "min_price": None, "max_price": None},
    {"section": "fua", "query":"dresser", "slack_channel":"dressers", "min_price": None, "max_price": 100},
    {"section": "zip", "query":"shel*", "slack_channel":"shelves", "min_price": None, "max_price": None},
    {"section": "fua", "query":"shel*", "slack_channel":"shelves", "min_price": None, "max_price": 40},
    {"section": "zip", "query":"bookcase", "slack_channel":"bookcases", "min_price": None, "max_price": None},
    {"section": "fua", "query":"bookcase", "slack_channel":"bookcases", "min_price": None, "max_price": 50},
    {"section": "zip", "query":"nightstand", "slack_channel":"nightstands", "min_price": None, "max_price": None},
]

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 5 * 60 # 5 minutes


# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "")



# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
