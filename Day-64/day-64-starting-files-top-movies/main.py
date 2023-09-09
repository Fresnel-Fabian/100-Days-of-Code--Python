from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


# TMDB bearer token
headers = {
            "accept": "application/json",
            "Authorization": "Bearer token"
        }
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
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
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
        movie_id = request.args.get('id')
        movie_to_updata = db.get_or_404(Movie, movie_id)
        movie_to_updata.rating = edit_form.rating.data
        movie_to_updata.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=edit_form)

# Flask form to add movie
# class AddMovie(FlaskForm):
#     title = StringField("Title", validators=[DataRequired()])
#     year = StringField("Year", validators=[DataRequired()])
#     description = StringField("Description", validators=[DataRequired()])
#     rating = StringField("Rating", validators=[DataRequired()])
#     ranking = StringField("Ranking", validators=[DataRequired()])
#     review = StringField("Review", validators=[DataRequired()])
#     img_url = StringField("Image URL", validators=[DataRequired()])
#     submit = SubmitField("Done")

# Flask form to find movie
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        title = title.replace(" ", "%20")
        url = f"https://api.themoviedb.org/3/search/movie?query={title}&include_adult=false&language=en-US&page=1"
        response = requests.get(url, headers=headers)
        data = response.json()["results"]
       
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)

@app.route("/selected/")
def selected():
    id = request.args.get("id")
    if id:
        url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
        response = requests.get(url, headers=headers)
        data = response.json()
        MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
        new_movie = Movie(
                title=data["title"],
                year=data["release_date"].split("-")[0],
                description=data["overview"],
                rating=0,
                ranking=0,
                review="",
                img_url=f"{MOVIE_DB_IMAGE_URL}/{data['poster_path']}"
                )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))
    return redirect(url_for('home'))


@app.route("/delete/<int:id>")
def delete(id):
    # movie_id  = request.args.get('id')
    movie_to_delete=db.get_or_404(Movie, id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
