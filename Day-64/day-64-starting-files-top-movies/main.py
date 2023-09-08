from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# Create app
app = Flask(__name__)
# Configure sqlite file path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
# Create extension
db = SQLAlchemy()
# Initialize extension
db.init_app(app)
# Set secret key
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Initialize bootstrap5
Bootstrap5(app)

# Create table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# Create table in db
with app.app_context():
    db.create_all()

# new_movie = Movie(
#     title = "Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone "\
#     "booth, pinned down by an extortionist's sniper rifle. Unable to leave "\
#     "or receive outside help, Stuart's negotiation with the caller leads to "\
#     "a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# new_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, "\
#     "learn the story of the Sully family (Jake, Neytiri, and their kids), the "\
#     "trouble that follows them, the lengths they go to keep each other safe, "\
#     "the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

@app.route("/")
def home():
    # Read and show data from database
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)

# Flask from to edit rating and review
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    edit_form = RateMovieForm()
    if edit_form.validate_on_submit():
        rating = edit_form.rating.data
        review = edit_form.review.data
        print(rating, review)
        movie_id = request.args.get('id')
        movie_to_updata = db.get_or_404(Movie, movie_id)
        movie_to_updata.rating = rating
        movie_to_updata.review = review
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form)

# Flask form to add movie
class AddMovie(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    ranking = StringField("Ranking", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Done")
@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovie()
    if add_form.validate_on_submit():
        new_movie = Movie(
            title=add_form.title.data,
            year=add_form.year.data,
            description=add_form.description.data,
            rating=add_form.rating.data,
            ranking=add_form.ranking.data,
            review=add_form.review.data,
            img_url=add_form.img_url.data,
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=add_form)

@app.route("/delete/<int:id>")
def delete(id):
    # movie_id  = request.args.get('id')
    movie_to_delete=db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
