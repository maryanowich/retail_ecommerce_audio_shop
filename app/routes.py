from flask import Blueprint, redirect

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return redirect("/admin")
