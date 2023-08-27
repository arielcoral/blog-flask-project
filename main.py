from flask import Flask, render_template
import requests

url = 'https://api.npoint.io/22aa215fedad3248f28c'

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url=url)
    posts = response.json()
    print(posts)
    return render_template("index.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:num>')
def post(num):
    response = requests.get(url)
    posts = response.json()
    the_post = None
    for post in posts:
        if post['id'] == num:
            the_post = post
            break
    return render_template("post.html", hpost=the_post)


if __name__ == "__main__":
    app.run(debug=True)