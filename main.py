from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/posts')
def posts():
    return render_template("posts.html")


@app.route('/albums')
def albums():
    return render_template("albums.html")


if __name__ == '__main__':
    app.run(debug=True)