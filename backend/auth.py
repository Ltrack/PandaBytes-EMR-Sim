from flask import Blueprint, render_template, request, redirect, url_for, make_response
from flask_login import UserMixin, login_user, logout_user, login_required, LoginManager
from dotenv import load_dotenv
import os

# from flask_bcrypt import Bcrypt
from flask import current_app
import json

# Create a Blueprint for authentication
auth = Blueprint("auth", __name__)
load_dotenv()

# Load user data
user_data_file = os.getenv("USER_DATA_FILE")
with open(user_data_file) as user_file:
    users = json.load(user_file)


# User class
class User(UserMixin):
    def __init__(self, id):
        self.id = id


login_manager = LoginManager()
login_manager.login_view = "auth.login"


# Routes
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form["username"]
        password = request.form["password"]
        # !implement better security
        if user_id in users and password == users[user_id]["password"]:
            user = User(user_id)
            login_user(user)
            return redirect(url_for("patient_list"))
        else:
            return redirect(url_for("auth.login"))
    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    # Prevent caching of the page by setting cache-control headers
    response = make_response(redirect(url_for("auth.login")))
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


@auth.route("/protected")
@login_required
def protected():
    return "This is a protected page. Only logged-in users can access it."


# User loader
@auth.app_context_processor
def inject_user_loader():
    def user_loader(user_id):
        if user_id not in users:
            return None
        user = User(user_id)
        return user

    return dict(user_loader=user_loader)
