from business import Product

import sqlite3
from contextlib import closing

conn = None

# connecting to the database
def connect():
    global conn
    if not conn:
        conn = sqlite3.connect("database.db", check_same_thread=False)
        conn.row_factory = sqlite3.Row
        print("successfully connected to conn inventory")


# close the connection
def close():
    if conn:
        conn.close()


# get number of items in the cart table to display on the home page
def get_number_of_items_in_cart():
    global conn
    connect()
    cur = conn.cursor()
    cur.execute("SELECT count(productId) FROM cart")
    number_of_items = cur.fetchone()[0]
    return number_of_items


# get all the products for display on the home page
def get_products():
    connect()
    global conn
    query = '''SELECT productId, name, price, description, image, stock FROM products'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()
    ans = []
    i = 0
    while i < len(results):
        curr = []
        for j in range(6):
            if i >= len(results):
                break
            product = Product(name=results[i]['name'], price=float(results[i]['price']), id=results[i]['productId'],
                              description=results[i]['description'], image=results[i]['image'], stock=int(results[i]['stock']))
            curr.append(product)
            i += 1
        ans.append(curr)
    print(len(ans))
    for i in ans:
        for x in i:
            x.print()
    return ans


def add_product_to_cart(product_id, quantity=1):
    global conn
    connect()
    sql = '''INSERT INTO cart (quantity, productID) VALUES (?, ?)'''
    with closing(conn.cursor()) as c:
        # try:
        c.execute(sql, (quantity, product_id))
        conn.commit()
        message = "Added successfully"
        # except:
        #     conn.rollback()
        #     message = 'Error occured'
        print(message)


def get_product_by_id(productID):
    global conn
    connect()
    sql = '''SELECT name, price, description, image, stock 
             FROM products WHERE productId = ?'''
    with closing(conn.cursor()) as c:
        try:
            c.execute(sql, (productID, ))
            productData = c.fetchone()
            product = Product(name=productData['name'], price=float(productData['price']), id=productID,
                              description=productData['description'], image=productData['image'], stock=int(productData['stock']))
            return product
        except:
            conn.rollback()
            message = "Error occured when getting a product by ID"
            print(message)


def get_products_in_cart():
    global conn
    connect()
    sql = '''SELECT products.productId, products.name, products.price, products.image 
             FROM products, cart WHERE products.productId = cart.productId'''
    with closing(conn.cursor()) as c:
        c.execute(sql)
        results = c.fetchall()
    products_list = []
    for row in results:
        product = Product(name=row['name'], price=float(row['price']), id=row['productId'], image=row['image'])
        products_list.append(product)
    return products_list

def clear_cart():
    global conn
    connect()
    query = '''DELETE FROM cart'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        conn.commit()


def remove_product_from_cart(productID):
    global conn
    connect()
    sql = '''DELETE FROM cart WHERE productId = ?'''
    with closing(conn.cursor()) as c:
        try:
            c.execute(sql, (productID, ))
            conn.commit()
            message = "Removed successfully"
        except:
            conn.rollback()
            message = 'Error occured when removing item from cart'


# add_product_to_cart(3, quantity=1)