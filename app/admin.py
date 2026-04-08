from flask import Blueprint, render_template, request, redirect, send_file
from app.models import Product

from app import db
import pandas as pd

admin = Blueprint("admin", __name__)

from flask import redirect

@admin.route("/")
def root_redirect():
    return redirect("/admin")

@admin.route("/admin")
def dashboard():
    products = Product.query.all()
    return render_template("admin/dashboard.html", products=products)

@admin.route("/admin/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":

        sku = request.form["sku"]
        name = request.form["name"]
        mpc = request.form["mpc"]
        sale_price = request.form["sale_price"]
        description = request.form["description"]
        stock = request.form["stock"]
        specs = request.form["specs"]

        brand = request.form["brand"]
        category = request.form["category"]
        weight = request.form["weight"]
        slug = request.form["slug"]

        active = True if request.form.get("active") else False
        featured = True if request.form.get("featured") else False

        file = request.files["image"]

        filename = None

        if file and file.filename != "":
            from werkzeug.utils import secure_filename
            import os

            filename = secure_filename(file.filename)
            filepath = os.path.join("static/images", filename)
            file.save(filepath)

        new_product = Product(
            sku=int(sku),
            name=name,
            brand=brand,
            category=category,
            mpc=float(mpc),
            sale_price=float(sale_price) if sale_price else None,
            stock=int(stock),
            weight=float(weight) if weight else None,
            description=description,
            specs=specs,
            slug=slug,
            active=active,
            featured=featured,
            image=filename
        )

        db.session.add(new_product)
        db.session.commit()

        return redirect("/admin")

    return render_template("admin/add_product.html")

@admin.route("/admin/edit/<int:id>", methods=["GET", "POST"])
def edit_product(id):
    product = Product.query.get_or_404(id)

    if request.method == "POST":
        product.sku = int(request.form["sku"])
        product.name = request.form["name"]
        product.brand = request.form["brand"]
        product.category = request.form["category"]
        product.mpc = float(request.form["mpc"])
        product.sale_price = float(request.form["sale_price"]) if request.form["sale_price"] else None
        product.stock = int(request.form["stock"])
        product.weight = float(request.form["weight"]) if request.form["weight"] else None
        product.description = request.form["description"]
        product.specs = request.form["specs"]
        product.slug = request.form["slug"]
        product.active = True if request.form.get("active") else False
        product.featured = True if request.form.get("featured") else False

        file = request.files.get("image")
        if file and file.filename != "":
            from werkzeug.utils import secure_filename
            import os
            filename = secure_filename(file.filename)
            filepath = os.path.join("static/images", filename)
            file.save(filepath)
            product.image = filename

        db.session.commit()
        return redirect("/admin")

    return render_template("admin/edit_product.html", product=product)

@admin.route("/admin/delete/<int:id>")
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/admin")

@admin.route("/admin/import", methods=["GET", "POST"])
def import_products():
    if request.method == "POST":
        file = request.files["file"]

        df = pd.read_excel(file)

        for _, row in df.iterrows():
            existing_product = Product.query.filter_by(sku=int(row["sku"])).first()

            if existing_product:
                # UPDATE existing product
                existing_product.name = row["name"]
                existing_product.brand = row["brand"]
                existing_product.category = row["category"]
                existing_product.mpc = float(row["mpc"])
                existing_product.sale_price = float(row["sale_price"]) if not pd.isna(row["sale_price"]) else None
                existing_product.stock = int(row["stock"])
                existing_product.weight = float(row["weight"]) if not pd.isna(row["weight"]) else None
                existing_product.description = row["description"]
                existing_product.specs = row["specs"]
                existing_product.slug = row["slug"]
                existing_product.active = bool(row["active"])
                existing_product.featured = bool(row["featured"])
                existing_product.image = row["image"]
            else:
                # INSERT new product
                product = Product(
                    sku=int(row["sku"]),
                    name=row["name"],
                    brand=row["brand"],
                    category=row["category"],
                    mpc=float(row["mpc"]),
                    sale_price=float(row["sale_price"]) if not pd.isna(row["sale_price"]) else None,
                    stock=int(row["stock"]),
                    weight=float(row["weight"]) if not pd.isna(row["weight"]) else None,
                    description=row["description"],
                    specs=row["specs"],
                    slug=row["slug"],
                    active=bool(row["active"]),
                    featured=bool(row["featured"]),
                    image=row["image"]
                )

                db.session.add(product)

        db.session.commit()

        return redirect("/admin")

    return render_template("admin/import.html")


# Route to download an Excel template for product import
@admin.route("/admin/template")
def download_template():
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active

    # Headers
    headers = [
        "sku", "name", "brand", "category",
        "mpc", "discount_percent", "sale_price",
        "stock", "weight", "description",
        "specs", "slug", "active", "featured", "image"
    ]

    ws.append(headers)

    # Example row with formula for sale_price
    ws.append([
        "", "", "", "",
        100, 15, "=E2*(1-F2/100)",
        "", "", "", "", "", "", "", ""
    ])

    import os
    from io import BytesIO

    file_stream = BytesIO()
    wb.save(file_stream)
    file_stream.seek(0)

    return send_file(
        file_stream,
        as_attachment=True,
        download_name="template.xlsx",
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Route to export all products to Excel
@admin.route("/admin/export")
def export_products():
    products = Product.query.all()

    data = []

    for p in products:
        data.append({
            "sku": p.sku,
            "name": p.name,
            "brand": p.brand,
            "category": p.category,
            "mpc": p.mpc,
            "sale_price": p.sale_price,
            "stock": p.stock,
            "weight": p.weight,
            "description": p.description,
            "specs": p.specs,
            "slug": p.slug,
            "active": p.active,
            "featured": p.featured,
            "image": p.image
        })

    df = pd.DataFrame(data)

    path = "export.xlsx"
    df.to_excel(path, index=False)

    return send_file(path, as_attachment=True)
