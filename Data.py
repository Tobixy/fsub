

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
Bot Users
  /start - Start
  /about - About
  /help - Help
  /ping - Bot Latency
  /uptime - Uptime

Bot Admins
  /logs - Logs
  /users - User Statistics
  /batch - Multi Post (Single Link)
  /broadcast - Broadcast Message
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
@{} is a Bot for storing posts or files that can be accessed through a special link.

  Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
  Re-Code From: <a href='https://github.com/mrismanaziz/File-Sharing-Man'>File-Sharing-Man</a>
"""
