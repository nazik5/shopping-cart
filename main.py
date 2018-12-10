from flask import *
import db
app = Flask(__name__)

@app.route("/")
def root():
    cart_num_of_items = db.get_number_of_items_in_cart()
    products = db.get_products()
    return render_template('home.html', itemData=products, noOfItems=cart_num_of_items)


@app.route("/productDescription")
def product_description():
    products_in_cart_count = db.get_number_of_items_in_cart()
    productID = request.args.get('productId')
    product = db.get_product_by_id(productID)
    return render_template("productDescription.html", data=product, noOfItems=products_in_cart_count)


@app.route("/addToCart")
def add_to_cart():
    productID = int(request.args.get('productId'))
    db.add_product_to_cart(productID)
    return redirect(url_for('root'))


@app.route("/cart")
def cart():
    products = db.get_products_in_cart()
    items_in_cart_count = db.get_number_of_items_in_cart()
    total_price = 0
    for product in products:
        total_price += product.price
    return render_template("cart.html", products=products, totalPrice=total_price, noOfItems=items_in_cart_count)


@app.route("/checkout")
def checkout():
    products = db.get_products_in_cart()
    db.clear_cart()
    items_in_cart_count = db.get_number_of_items_in_cart()
    total_price = 0
    for product in products:
        total_price += product.price
    return render_template("checkout.html", products=products, totalPrice=total_price, noOfItems=items_in_cart_count)


@app.route("/removeFromCart")
def removeFromCart():
    productID = int(request.args.get('productId'))
    db.remove_product_from_cart(productID)
    return redirect(url_for('root'))


if __name__ == '__main__':
    app.run(debug=True)
