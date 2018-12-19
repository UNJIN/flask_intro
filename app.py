from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>asdfasdfasdf</h1>"

@app.route("/html_tag")
def html_tag():
    return """
    <h1>asdf</h1>
    <h2>aasdfsdf</h2>
    """

@app.route("/html_file")
def html_file():
    return render_template("html_file.html")

@app.route("/welcome/<int:num>")
def welcome(num):
    return render_template("welcome.html", p = num)
    