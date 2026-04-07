from flask import Blueprint, render_template
from app.models import Product

main = Blueprint("main", __name__)

@main.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)
