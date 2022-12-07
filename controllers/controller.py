from flask import render_template
from app import app
from models.order_list import orders

@app.route('/orders')
def index():
    return render_template('index.html', title="Current Orders", orders_html=orders)

@app.route('/orders/<index>')
def order(index):
    page_title = f"Order: {orders[int(index)].customer_name}"
    return render_template('order.html', title=page_title, order_html=orders[int(index)])