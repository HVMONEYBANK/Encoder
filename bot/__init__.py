import os
import logging
import asyncio
from logging.handlers import RotatingFileHandler
from pyrogram import Client
from dotenv import load_dotenv

LOG_FILE_NAME = "Encoder@Log.txt"

if os.path.exists(LOG_FILE_NAME):
    with open(LOG_FILE_NAME, "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=2097152000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("urllib3").setLevel(logging.INFO)
LOGS = logging.getLogger(__name__)


THUMB = "https://te.legra.ph/file/2ebf402cdef8c27ab4648.jpg"
os.system(f"wget {THUMB} -O thumb.jpg")
ffmpeg = []
ffmpeg.append("-i 'https://telegra.ph/file/ab2c66f1192454112150d.png' -i input_video.mp4 -filter_complex '[1:v][0]overlay=W-w-10:H-h-10[out]' -map '[out]' -c:v libx265 -crf 30 -c:s copy -s 1280x720 -preset veryfast -metadata title='Visit For More Cartoons [t.me/HV_CARTOONS_TELUGU_2]' -metadata:s:v title='Visit Website[HV CARTOONS] t.me/AniXpo] - 720p - HEVC - 8bit' -metadata:s:a title='[Visit t.me/HV_CARTOONS_TELUGU_2] - Opus - 60 kbps' -metadata:s:s title='[AniXpo Substations Alpha]' -c:a libopus -ab 60k -vbr 2 -ac 2 -level 2.1")
try:
 api_id = int(os.environ.get("API_ID"))
 api_hash = os.environ.get("API_HASH")
 bot_token = os.environ.get("BOT_TOKEN")
 DATABASE_URL = os.environ.get("DATABASE_URL") 
 BOT_USERNAME = "neswtsbot"
 MAX_MESSAGE_LENGTH = 4096
 download_dir = os.environ.get("DOWNLOAD_DIR", "downloads/")
 sudo_users = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
 sudo_users.append(1099725030)
 sudo_users.append(5089884151)
 LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
except Exception as e:
 LOGS.info("ENV Are Missing")

app = Client("nirusaki", api_id=api_id, api_hash=api_hash, bot_token=bot_token, workers=2)
0
data = []

if not download_dir.endswith("/"):
  download_dir = str(download_dir) + "/"
if not os.path.isdir(download_dir):
  os.makedirs(download_dir)
