from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18960528"))
API_HASH = getenv("API_HASH", "cc0fff577b677c9b2b4de5dd5bc5dfd1")
BOT_TOKEN = getenv("BOT_TOKEN", "5624068661:AAELqSx1Kqx2tTwwDzDVtfr5Xr0Dja9WV5g")
BOT_NAME = getenv("BOT_NAME","MUSICOLET MUSIC BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "MUSICOLET_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "shubhamsah1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "the_chatting")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/8b0e67ada4f97299ad60a.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/8b0e67ada4f97299ad60a.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQBQeWKynSh7yHDzZX6Fd7mdGjVvHnrPNf4X2cG5tP7BU9C74adpT8f9EYW6y6PCQx7ccmWuwz2VzloEovD_UmnoCvCZXwNcmDYDSJsgZV_gkFQcT1RhYTCIboh3pGCmgdS9uGlD_1c37kQX1LSXbSKeEHvt8b0TAsVKb0WyuMYXHWy0VeL4By2mtMEin8dyZW8IG6oLCKIBez_wPy7Ev3H1tOhWcU1ja-8yB6nsSr4YAMZxAxJzudnwuj1EHfx0jm6gZccJ5c8qy4rbnhtW7kGc2GIiCUahIR82aaW33_-JEMZwH14g08k5d_TFiRn8gbzRbaBmv2lsTUjsg85xTF1TAAAAAWTB-fAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5853904565").split()))
