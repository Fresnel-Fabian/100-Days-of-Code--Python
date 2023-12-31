from flask import Flask, render_template, request
import requests
import smtplib


MY_PASSWORD = " "
MY_EMAIL = "fresnelfabian@gmail.com"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json").json()


app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    send = False
    if request.method == 'POST':
        data = request.form
        print(data["name"], data["email"], data["phone"], data["message"], sep="\n")
        send = True
        send_email(data=data)
    return render_template("contact.html", send=send)

def send_email(data):
    email_message = f"Subject:New Message\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
    print(email_message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form["name"]
#     email = request.form["email"]
#     phone = request.form["phone"]
#     message = request.form["message"]
#     print(name, email, phone, message)
#     return "Success"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
