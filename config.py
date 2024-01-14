

from os import environ
from dotenv import load_dotenv
from distutils.util import strtobool
from logging.handlers import RotatingFileHandler
from logging import (
    basicConfig,
    INFO,
    WARNING,
    StreamHandler,
    getLogger,
    Logger,
)

load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN", "")

CHANNEL_DB = int(environ.get("CHANNEL_DB", ""))
DATABASE_URL = environ.get("DATABASE_URL", "")
DATABASE_NAME = environ.get("DATABASE_NAME", "")

RESTRICT = strtobool(environ.get("RESTRICT", "True"))

FORCE_SUB_ = {}
FSUB_TOTAL = 1
while True:
    key = f"FORCE_SUB_{FSUB_TOTAL}"
    value = environ.get(key)
    if value is None:
        break
    FORCE_SUB_[FSUB_TOTAL] = int(value)
    FSUB_TOTAL += 1

BUTTON_ROW = int(environ.get("BUTTON_ROW", "3"))
BUTTON_TITLE = environ.get("BUTTON_TITLE", "Join")

START_MESSAGE = environ.get(
    "START_MESSAGE",
    "Hello {mention}!"
    "\n\n"
    "I can store private files in a specific Channel, and other users can access them through a special link.",
)
FORCE_MESSAGE = environ.get(
    "FORCE_MESSAGE",
    "Hello {mention}!"
    "\n\n"
    "You must join the Channel/Group first to view the files I share."
    "\n\n"
    "Please join the Channel/Group first.",
)

try:
    ADMINS = [int(x) for x in (environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Your Admins list does not contain valid Telegram User IDs.")

CUSTOM_CAPTION = environ.get("CUSTOM_CAPTION", None)
DISABLE_BUTTON = strtobool(environ.get("DISABLE_BUTTON", "False"))

LOGS_FILE = "logs.txt"
basicConfig(
    level=INFO,
    format="[%(levelname)s] - %(message)s",
    handlers=[
        RotatingFileHandler(LOGS_FILE, maxBytes=50000000, backupCount=10),
        StreamHandler(),
    ],
)
getLogger("pyrogram").setLevel(WARNING)


def LOGGER(name: str) -> Logger:
    return getLogger(name)
