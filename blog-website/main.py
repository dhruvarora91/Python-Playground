from flask import Flask, render_template
import requests
from post import Post

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
posts = response.json()
posts_objects = []
for post in posts:
    posts_objects.append(Post(post))

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts_objects)


@app.route("/post/<int:id>")
def posts_page(id):
    for post in posts_objects:
        if post.id == id:
            return render_template("post.html", post=post)
    return "<h1>No post found with this id</h1>"


if __name__ == "__main__":
    app.run(debug=True)
