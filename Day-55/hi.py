from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        string = func
        return f"<b>{string}</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        string = func
        return f"<em>{string}</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        string = func
        return f"<u>{string}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello World!</h1>"\
    "<p>This is a paragraph.</p>"\
    "<img src='https://media.giphy.com/media/4Iw2OzgiiTc4M/giphy.gif', width=500>"


@app.route("/username/<name>")
@make_bold
@make_emphasis
@make_underlined
def hello(name):
    return f"Hello {name}"


@app.route("/profile/<int:profile_id>")
def show_profile(profile_id):
    return f"You are in {profile_id}"

@app.route("/<path:subpath>")
def show_subpath(subpath):
    return f"You are in path {subpath}"

if __name__ == "__main__":
    app.run(debug=True)