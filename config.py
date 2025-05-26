import os
from telethon import TelegramClient
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

def get_env_or_fail(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"{key} is not set in environment variables")
    return value

# Bot Metadata
BOT_NAME = os.getenv("BOT_NAME", "𝐒𝐓𝐑𝐀𝐍𝐄𝐑 𝐒𝐏𝐀𝐌")
BOT_LOGO = os.getenv("BOT_LOGO", "https://telegra.ph/file/aa4bf1e57d11fb75b602e.jpg")
KEYWORDS = os.getenv("KEYWORDS", "telegram,telethon,telegram-bot,PythonX,SpamBots").split(',')
REPOSITORY = os.getenv("REPOSITORY", "https://github.com/GENZ-ARSH/ARSH-SPAM-X")

# Required values
API_ID = int(get_env_or_fail("API_ID"))
API_HASH = get_env_or_fail("API_HASH")
OWNER_ID = int(get_env_or_fail("OWNER_ID"))

# Optional values with defaults
CMD_HNDLR = os.getenv("CMD_HNDLR", ".")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

# Bot tokens
BOT_TOKEN = get_env_or_fail("BOT_TOKEN")
BOT_TOKEN2 = get_env_or_fail("BOT_TOKEN2")
BOT_TOKEN3 = get_env_or_fail("BOT_TOKEN3")
BOT_TOKEN4 = get_env_or_fail("BOT_TOKEN4")
BOT_TOKEN5 = get_env_or_fail("BOT_TOKEN5")
BOT_TOKEN6 = get_env_or_fail("BOT_TOKEN6")
BOT_TOKEN7 = get_env_or_fail("BOT_TOKEN7")
BOT_TOKEN8 = get_env_or_fail("BOT_TOKEN8")
BOT_TOKEN9 = get_env_or_fail("BOT_TOKEN9")
BOT_TOKEN10 = get_env_or_fail("BOT_TOKEN10")

# Sudo users
SUDO_USERS = []
sudo_users_str = os.getenv("SUDO_USER", "")
if sudo_users_str:
    SUDO_USERS.extend(int(x) for x in sudo_users_str.split())

# Add owner to sudo users
SUDO_USERS.append(OWNER_ID)
# Add additional sudo users
SUDO_USERS.extend([6919199044, 6762113050, 6876910746])

# Database
DB_URI = os.getenv("DATABASE_URL")

# PostgreSQL Version
POSTGRES_VERSION = os.getenv("POSTGRES_VERSION", "15")

# Initialize Telegram Clients
MK1 = TelegramClient('MK', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
MK2 = TelegramClient('MK2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
MK3 = TelegramClient('MK3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
MK4 = TelegramClient('MK4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
MK5 = TelegramClient('MK5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
MK6 = TelegramClient('MK6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
MK7 = TelegramClient('MK7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
MK8 = TelegramClient('MK8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
MK9 = TelegramClient('MK9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
MK10 = TelegramClient('MK10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
