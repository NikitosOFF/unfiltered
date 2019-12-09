from typing import List, Dict

LIKE_EMOJI_NAME = '+1'
DISLIKE_EMOJI_NAME = '-1'

REACT_REMINDER = (
    "You don't appreciate solving of your problem, "
    'please react with emojis right now for {0}'
)

REMIND_REACT_FOR_DAYS = 1

IS_DEBUG_ENABLED = False

ATTENDANTS: List[Dict[str, str]] = []
SLACK_CHANNEL_ID = ''
DEBUG_SLACK_CHANNEL_ID = ''
SLACK_CHANNEL_BOT_ID = ''
SLACK_TOKEN = ''

try:
    from .local_config import *  # noqa:F401,F403
except ImportError:
    pass
