from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
# Create database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# Create teh extension
db = SQLAlchemy()
# initialise the app with the extension
db.init_app(app)

# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form
        # Create record
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        print(dict(data))
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit/<number:int>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        book_to_update = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html")
if __name__ == "__main__":
    app.run(debug=True)

