# SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)
# define model
class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
with app.app_context():
    db.create_all()
    # # Create a entry
    # book = books(
    #     title = "Narnia",
    #     author = "C. S. Lewis",
    #     rating = "10"
    # )
    # db.session.add(book)
    # db.session.commit()
# Read from db
with app.app_context():
    result = db.session.execute(db.select(books).order_by(books.title)).scalars()
    print(result)
