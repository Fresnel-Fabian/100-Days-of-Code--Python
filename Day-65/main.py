from flask import Flask, render_template

app = Flask(__name__)

app.route("/")
def home():
    return "hello"

if __name__ == "__main__":
    app.run()

print("hello")
print("world")
print("hell")