from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def home ():
	return render_template("home.html")

@app.route("/store")
def store ():
	return render_template("store.html")

@app.route("/cart", methods=['GET','POST'])
def cart ():
	return render_template("cart.html")

@app.route('/add_to_cart/<int:pid>')
def addToCart(pid):
	add_to_cart(pid)
	print ("Added product number: " + pid + " to cart.")
	return redirect(url_for('store'))

@app.route("/about")
def about ():
	return render_template("about.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)