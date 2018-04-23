from flask import render_template, request, redirect, url_for
from app import models
from app import app, member_store, post_store

@app.route("/",methods=["GET","POST"])
def login_page():
    database = {"admin@gmail.com":"root"}
    if request.method =="POST":
        if database.get(str(request.form["username"])) == str(request.form["password"]):
            return redirect(url_for("home"))
    return render_template("Signin.html")
@app.route("/index")    
def home():
    posts = post_store.get_all()
    members = member_store.get_all()
    return render_template("index_2.html",posts = posts ,members=members)

@app.route("/add_post",methods= ["GET","POST"])
def add_post():
    if request.method == "POST":
        new_post = models.Post(title=request.form["Title"], content=request.form["Content"])
        post_store.add(new_post)
        return redirect(url_for("home"))
    else:
        return render_template("add_post.html")
@app.route("/members")
def members():
    return render_template("members.html",members=member_store.get_all())
@app.route("/post")
def get_post():
    return render_template("posts.html",post= post_store.get_all())
@app.route("/contact")
def contact_us():
    return render_template("contact.html")
@app.route("/topic/delete/<int:id>")
def delete_post(id):
    post_store.delete(id)
    return redirect(url_for("home"))

