from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, link, description)

	Product_object = Product(
		name=name,
		price=price,
		link=link,
		description=description)
	session.add(Product_object)
	session.commit()

add_product("phone","3000","iphone.jpeg", "smart phone")

def edit_by_id(id)
	Product_object = session.query(
		product).filter_by(id=id).first()