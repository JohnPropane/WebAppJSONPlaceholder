from flask import Flask, render_template, request
import web_functions

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST':
        num_of_posts = int(request.form['max-posts'])
        min_len = int(request.form['min-len'])
        max_len = int(request.form['max-len'])
        data = web_functions.generate2(num_of_posts, min_len, max_len)
    else:
        num_of_posts = 100
        data = web_functions.generate2(num_of_posts)
    return render_template('posts.html', data=data)


@app.route('/albums')
def albums():
    return render_template("albums.html")


if __name__ == '__main__':
    app.run(debug=True)
    
