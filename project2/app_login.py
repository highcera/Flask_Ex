# from ctypes.wintypes import PWCHAR
from flask import Flask, render_template, request, redirect, url_for, session

# import sys
# import database

app = Flask(__name__)
app.scret_key = "dark##2993"

ID = "hello"
PW = "world"

@app.route("/")
def home():
    if "userID" in session:
        return render_template("home.html", username = session.get("userID"), login = True)
    else:
        return render_template("home.html", login = False)

@app.route("/login", methods = ["get"])
def login():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if _id_ == ID and _password_ == PW:
        session["userID"] == _id_
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))
   
@app.route("/logout")
def logout():
    session.pop("useID")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()