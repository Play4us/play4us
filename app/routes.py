from flask import render_template
import requests

from app import app
from app import signin

@app.route('/')
@app.route('/index')
def index():
    return signin.signin_page()

@app.route("/login")
def login():
    return signin.login()

@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
