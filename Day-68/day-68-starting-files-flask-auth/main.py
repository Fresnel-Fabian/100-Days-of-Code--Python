from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# initialize flask login
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
 
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Hashing and salting the password entered by the user
        password = generate_password_hash(
            request.form.get("password"), 
            method='pbkdf2:sha256', 
            salt_length=8
        )
        # Storing the hashed password in our database
        new_user = User(
            email = request.form["email"],
            name = request.form["name"],
            password = password,
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets", email=new_user.email))
    
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login_user()
    return render_template("login.html")


@app.route('/secrets/<string:email>')
def secrets(email):
    user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    return render_template("secrets.html", user=user)


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory(
        'static', path="files/cheat_sheet.pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
