from flask import Blueprint, render_template, abort, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Blog
from .forms import CreateBlogForm
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def home():
    posts = db.session.execute(db.select(Blog)).scalars()
    return render_template("index.html", posts=posts)

@main.route("/post/<int:post_id>/")
def post(post_id):
    post = db.get_or_404(Blog, post_id)
    return render_template("post.html", post=post)

# EDIT FUNCTION WITHOUT WTFORMS
# @main.route("/edit/<int:post_id>/", methods=["GET", "POST"])
# def edit(post_id):
#     post = db.get_or_404(Blog, post_id)
#     if request.method == "POST":
#         title = request.form.get("title")
#         body = request.form.get("body")
#         if title and body:
#             post.title = title
#             post.body = body
#             db.session.commit()
#             flash("Post updated successfully", "success")
#             return redirect(url_for("main.post", post_id=post.id))
#         flash("Title and Content are both required!", "warning")
#     return(render_template("edit.html", post=post))

# EDIT FUNCTION WITH WTFORMS
@main.route("/edit/<int:post_id>/", methods=["GET", "POST"])
def edit(post_id):
    post = db.get_or_404(Blog, post_id)
    if post.author != current_user:
        return abort(403)
    form = CreateBlogForm(
        title = post.title,
        body = post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash("Post updated successfully.", "success")
        return redirect(url_for("main.post", post_id=post_id))
    return(render_template("create.html", form=form, edit=True))

@main.route("/create/", methods=["GET", "POST"])
@login_required
def create():
    # NO WTFORMS
    # if request.method == "POST":
    #     title = request.form.get("title")
    #     body = request.form.get("body")
    #     if title and body:
    #         new_post = Blog(title=title, body=body)
    #         db.session.add(new_post)
    #         db.session.commit()
    #         return redirect(url_for('main.home'))
    #     flash("Title and Content are both required!", "warning")
    # return render_template("create.html")

    # WITH WTFORMS
    form = CreateBlogForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        author = current_user  # updated: now I have User model and Login functionality.
        new_post = Blog(title=title, body=body, author=author)
        db.session.add(new_post)
        db.session.commit()
        flash("New post created successfully!", "success")
        return redirect(url_for('main.home'))
    return render_template("create.html", form=form, edit=False)

@main.route('/delete/<int:post_id>/')
def delete(post_id):
    post = db.get_or_404(Blog, post_id)
    if post.author != current_user:
        return abort(403)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("main.home"))