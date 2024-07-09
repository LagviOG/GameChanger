from flask import render_template, redirect,flash
from forms import RegisterForm, LoginForm, PostForm
from ext import app
from os import path
from models import db, User
from flask_login import login_user, logout_user, login_required
from models import Game




@app.route("/")
def home():
    games = Game.query.all()
    return render_template("home.html", games = games)


@app.route('/Register', methods=["GET", "POST"])
def Register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user:
            username_taken = True
        else:
            username_taken = False
            new_user = User(username=form.username.data, password=form.password.data, role="guest")
            new_user.create()
            return redirect("/Login")
        return render_template("register.html", form=form, username_taken=username_taken)
    return render_template("register.html", form=form)



@app.route("/About/<name>")
def About(name):
    return render_template("about.html", user=name)


@app.route("/Login", methods=["GET", "POST"])
def Login():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        user = User.query.filter(User.username == loginform.username.data).first()
        if user:
            login_user(user)
            return redirect("/")
        else:
            flash("An account with this password and username doesn't exist")

    return render_template("login.html", loginform=loginform)





@app.route("/Post", methods=["GET", "POST"])
@login_required
def Post():
    postform = PostForm()
    if postform.validate_on_submit():
        new_game = Game(name=postform.game_name.data, description=postform.description.data)

        image = postform.game_img.data
        directory = path.join(app.root_path, "static", "photos", image.filename)
        image.save(directory)
        new_game.img = image.filename

        db.session.add(new_game)
        db.session.commit()
        return redirect("/")

    return render_template("post.html", postform=postform)


@app.route("/delete_game/<int:game_id>", methods=["GET", "POST"])
def delete_game(game_id):
    game = Game.query.get(game_id)

    db.session.delete(game)
    db.session.commit()
    return redirect("/")

@app.route("/game/<int:game_id>", methods=["GET", "POST"])
def game(game_id):
    game = Game.query.get(game_id)
    return render_template("game_details.html", game=game)

@app.route("/Logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect("/")
