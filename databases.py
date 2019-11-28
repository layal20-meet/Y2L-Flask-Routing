from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, link, description):

	Product_object = Product(
		name=name,
		price=price,
		link=link,
		description=description)
	session.add(Product_object)
	session.commit()

# add_product("phone","3000","iphone.jpeg", "smart phone")

def delete(id):
	session.query(product).filter_by(id=id).delete()
	session.commit()

def query_all():
	products = session.query(product).all()
	return products

def return_id(id):
	session.query(product).filter_by(id=id).first()
	return product

def add_to_cart(productID):
	productID_object = Cart(
		productID = productID)
	session.add(productID_object)
	session.commit()


