from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .forms import CreateUserForm, LoginUserForm
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/register/', methods=["GET", "POST"])
def register():
    form = CreateUserForm()
    if form.validate_on_submit():
        email = form.email.data
        suspected_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if suspected_user:
            print(suspected_user, "already exists")
            flash("You've already signed up with that email, log in instead!", "info")
            return redirect(url_for("auth.login"))

        name = form.name.data
        password = generate_password_hash(form.password.data)
        new_user = User(email=email, name=name, password=password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("You've successfully created your new account", "success")
        return redirect(url_for("main.home"))
    return render_template("register.html", form=form)

@auth.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginUserForm()
    if form.validate_on_submit():
        email = form.email.data
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not user:
            flash("The user does not exist yet, sign up.", "info")
            return redirect(url_for("auth.register"))
        password = form.password.data
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash("Wrong credentials, try again.", "warning")
    return render_template("login.html", form=form)

@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    return render_template("logout.html")

@auth.route("/profile/")
@login_required
def profile():
    return render_template("profile.html")
