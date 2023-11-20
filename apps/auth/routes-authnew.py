from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from apps.auth import blueprint
from apps.models.db_models import Users, Roles, ROLES
from werkzeug.security import check_password_hash, generate_password_hash

from apps import db


@blueprint.route("/")
def route_default():
    return redirect(url_for("auth_bp.login"))


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home_bp.home"))

    if "login" in request.form:
        # get email and password inputs
        email = request.form["email"]
        password = request.form["password"]

        # query database for inputted email
        user = db.session.query(Users).filter_by(UserEmail=email).first()

        valid, email_msg, pw_msg = False, None, None
        if not user:
            email_msg = "Account does not exist."
        elif not check_password_hash(user.PasswordHash, password):
            pw_msg = "Incorrect password, please try again."
        else:
            valid = True
        if not valid:
            return render_template(
                "accounts/login.html",
                user=current_user,
                email_msg=email_msg,
                pw_msg=pw_msg,
            )

        flash("Logged in successfully!", category="success")
        login_user(user, remember=True)
        return redirect(url_for("auth_bp.route_default"))

    return render_template("accounts/login.html", user=current_user)


@blueprint.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth_bp.login"))


@blueprint.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # if not current_user.is_manager():
    #     flash("You do not have access to create new users", category="error")
    #     return redirect(url_for("auth_bp.route_default"))

    # role_list = {
    #     r.id: r.Roles
    #     for r in db.session.query(Roles)
    #     .filter(Roles.id <= current_user.AccessLevel)
    #     .all()
    # }

    if request.method == "POST":
        email = request.form["email"]
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        role = request.form["role"]
        print(request.form.to_dict())

        user = db.session.query(Users).filter_by(UserEmail=email).first()

        valid, msg = False, ""
        if user:
            msg = "Email already exists."
        elif len(email) < 4:
            msg = "Email must be greater than 3 characters."
        elif len(first_name) < 2:
            msg = "First name must be greater than 1 character"
        elif password1 != password2:
            msg = "Passwords do not match!"
        elif len(password1) < 8:
            msg = "Password is too short!"
        else:
            valid = True

        if not valid:
            flash(msg, category="error")
            return redirect(url_for("auth_bp.sign_up"))

        new_user = Users(
            UserEmail=email,
            PasswordHash=generate_password_hash(password1, method="sha256"),
            FirstName=first_name,
            LastName=last_name,
            Role=int(role),
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully!", category="success")

    return render_template(
        "accounts/sign_up.html",
        user=current_user,
        role_list=['Dev']
    )


@blueprint.route("/change-password", methods=["GET", "POST"])
@login_required
def change_pwd():
    if request.method == "POST":
        old_password = request.form["password1"]
        new_password = request.form["password2"]
        new_confirmed = request.form["password3"]

        if not check_password_hash(current_user.PasswordHash, old_password):
            flash("Incorrect Old Password", category="error")
        elif new_password != new_confirmed:
            flash("New Passwords do not match, Try again", category="error")
        elif len(new_password) < 8:
            flash("Password is too short!", category="error")
        else:
            current_user.PasswordHash = generate_password_hash(
                new_password, method="sha256"
            )
            db.session.commit()
            flash("Password Changed Successfully", category="success")

    return render_template("accounts/change_pwd.html", user=current_user)


@blueprint.route("/reset-password", methods=["GET", "POST"])
@login_required
def reset_pwd():
    user_list = {u.id: u.UserEmail for u in db.session.query(Users).all()}
    if request.method == "POST":
        new_password = request.form.get("new_password")
        new_confirmed = request.form.get("confirm_password")
        idiot_id = request.form.get("idiot")

        if new_password != new_confirmed:
            flash("New Passwords do not match, Try again", category="error")
        elif len(new_password) < 8:
            flash("Password is too short!", category="error")
        else:
            idiot = db.session.query(Users).filter_by(id=idiot_id).first()
            idiot.PasswordHash = generate_password_hash(new_password, method="sha256")
            db.session.commit()
            flash("Password Changed Successfully", category="success")

    return render_template(
        "accounts/reset_pwd.html", user=current_user, user_list=user_list
    )


@blueprint.route("/change-access", methods=["GET", "POST"])
@login_required
def change_access():
    if not current_user.is_manager():
        flash("You do not have access to modify existing users roles", category="error")
        return redirect(url_for("home_bp.home"))

    user_role_list = {
        u.UserEmail: u.AccessLevel
        for u in db.session.query(Users)
        .filter(
            Users.AccessLevel <= current_user.AccessLevel, Users.id != current_user.id
        )
        .all()
    }

    # role_list = {
    #     r.id: r.UserRole
    #     for r in db.session.query(AccessLevel)
    #     .filter(AccessLevel.id <= current_user.AccessLevel)
    #     .all()
    # }

    if request.method == "POST":
        user_details = {request.form["user"]: request.form["new-role"]}

        db.session.query(Users).filter(Users.UserEmail.in_(user_details)).update(
            {Users.AccessLevel: case(user_details, value=Users.UserEmail)},
            synchronize_session=False,
        )
        db.session.commit()

        return redirect(url_for("auth_bp.change_access"))

    return render_template(
        "accounts/change-access.html",
        user_role_list=user_role_list,
        role_list=role_list,
        user=current_user,
    )

