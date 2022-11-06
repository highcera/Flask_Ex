from flask import Flask, render_template, request, redirect, url_for
import sys
import database

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("hello.html")

@application.route("/apply")
def apply():
    return render_template("apply.html")

@application.route("/applyphoto")
def photo_apply():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    built_in = request.args.get("built")
    if cleaness == None:
        cleaness = False
    else:
        cleaness = True

    # print(location, cleaness, built_in)
    database.save(location, cleaness, built_in)
    return render_template("apply_photo.html")

@application.route("/upload_done", methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    # print(database.now_index())
    uploaded_files.save("C:/stockauto/flask/project2/static/img/{}.jpeg".format(database.now_index()))
    return redirect(url_for("hello"))
    
@application.route("/list")
def list():
    house_list = database.load_list()
    length = len(house_list)
    # print(house_list, length)
    return render_template("list.html", house_list = house_list, length = length)

@application.route("/house_info/<int:index>/")
def house_info(index):
    house_info = database.load_house(index)
    location = house_info["location"]
    cleaness = house_info["cleaness"]
    built_in = house_info["built_in"]

    photo = f"img/{index}.jpeg"

    # print(location, cleaness, built_in, photo)
    return render_template("house_info.html", location = location, cleaness = cleaness, built_in = built_in, photo = photo)
    
if __name__ == "__main__":
    application.run()