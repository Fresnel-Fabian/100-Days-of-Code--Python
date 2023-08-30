from flask import Flask, render_template
import requests


post_data = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()
print(post_data)

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html", title="Home", post_data=post_data)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/post/<int:index>")
def post(index):
    for post in post_data:
        if post["id"] == index:
            print(post)
            post_ = post
            break
    return render_template("post.html", post=post_, image_url = post["image"])

if __name__ == "__main__":
    app.run(debug=True)