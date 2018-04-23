from flask import abort, jsonify
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all/")
def topic_get_all_api():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)

@app.route("/api/topic/add/", methods = ["POST"])
def topic_create_api():
  request_data = request.get_json()
  new_post = models.Post(title=request_data["title"], content=request_data["content"])
  post_store.add(new_post)
  return jsonify(new_post.__dict__())

@app.route("/api/topic/delete/<int:id>/", methods = ["DELETE"])
def topic_delete_api(id):
    post_store.delete(id)
    return jsonify("Post has been deleted!")
@app.route("/api/member/all/")
def get_members_api():
    members=[ member.__dict__() for member in  member_store.get_all()]
    return jsonify(members)

@app.route("/api/member/posts/<int:id>/", methods=["PUT"])
def get_Mposts_api(id):

    request_data = request.get_json()
    post = post_store.get_by_id(id)
    print(post)
    try:
        post.title = request_data["title"]
        post.content = request_data["content"]
        post_store.update(post)
        result = jsonify(post.__dict__())
    except AttributeError as b:
        print(b)
        result = abort(404, f"topic with id: {id} doesn't exist")
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")

    return result

@app.route("/api/topic/show/<int:id>")
def topic_show_api(id):
    post = post_store.get_by_id(id)
    try:
        result = jsonify(post.as_dict())
    except AttributeError:
        result = abort(404, f"topic with id: {id} doesn't exist")

    return result