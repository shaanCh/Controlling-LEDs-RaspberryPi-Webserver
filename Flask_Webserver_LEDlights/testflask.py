#!usr/bin/env/python3

from flask import Flask,render_template,request,url_for,redirect,session
app = Flask(__name__)
app.secret_key = "bruh"

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
	if request.method == "POST":
		user = request.form["nm"]
		session['user_name'] = user
		return redirect(url_for("user"))
	else:
		if "user_name" in session:
			return redirect(url_for("user"))
		return render_template("login.html")
@app.route("/user")
def user():
	if "user_name" in session:
		user = session["user_name"]
		return f"<h1>{user}</h1>"
	else:
		return redirect(url_for("login"))
@app.route("/logout")
def logout():
	session.pop("user_name", None)
	return redirect(url_for("login"))

if __name__ == "__main__":
	app.run(debug=True)
