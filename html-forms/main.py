from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

# https://flask.palletsprojects.com/en/2.1.x/quickstart/#:~:text=request.method%20%3D%3D%20%27POST%27-,The%20Request%20Object,-%C2%B6


@app.route('/login', methods=["POST"])
def login_page():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        return f"<h1>Email: {email} Password: {password}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
