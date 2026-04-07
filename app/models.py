from app import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # CORE
    sku = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100))

    # PRICING
    mpc = db.Column(db.Float)  # maloprodajna cijena
    sale_price = db.Column(db.Float)

    # STOCK
    stock = db.Column(db.Integer)

    # CONTENT
    description = db.Column(db.Text)
    specs = db.Column(db.Text)
    image = db.Column(db.String(200))

    # ORGANIZATION
    brand = db.Column(db.String(100))
    category = db.Column(db.String(100))

    # BUSINESS LOGIC
    active = db.Column(db.Boolean, default=True)
    featured = db.Column(db.Boolean, default=False)

    # SEO / SYSTEM
    slug = db.Column(db.String(200))
    weight = db.Column(db.Float)

    # AUDIT
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)