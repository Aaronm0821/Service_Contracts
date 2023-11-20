from flask import render_template
from flask_login import login_required, current_user
from apps.home import blueprint


@blueprint.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home/home.html", user=current_user, segment="home")
