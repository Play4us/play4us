from flask import Flask
import sys
sys.path.append("../")

app = Flask(__name__)

from app import routes
from app.database.user import User
from app.database.db import init_db_command
from app import signin
from app.bots.slack import slack_bot
