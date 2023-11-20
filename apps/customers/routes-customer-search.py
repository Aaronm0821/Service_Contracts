from flask import render_template
from flask_login import login_required, current_user

from apps.customers import blueprint
from models.models import Machines


@blueprint.route("/customers", methods=["GET", "POST"])
@login_required
def customer_search():
    temp = Machines.get_machines()

    for i in temp:

        return render_template(
            "customers/customer_search.html",
            user=current_user,
            customer_table=Machines.get_machines()
        )

    # if not current_user.is_authenticated:
    #     return redirect(url_for("auth_bp.sign_up"))

    # return render_template(
    #     "customers/customer_search.html",
    #     user=current_user,
    #     segment="customer_search"
    # )


@blueprint.route("/customer-add", methods=["GET", "POST"])
@login_required
def customer_add():
    return render_template(
        "customers/customer_add.html",
        user=current_user,
        segment="customer_add"
    )


@blueprint.route("/customer-update", methods=["GET", "POST"])
@login_required
def customer_update():
    return render_template(
        "customers/customer_update.html",
        user=current_user,
        segment="customer_update"
    )


@blueprint.route("/customer-details/<machine_id>", methods=["GET", "POST"])
@login_required
def customer_details(machine_id):
    print('sappo')

    return render_template(
        "/customers/customer_details.html",
        user=current_user,
        segment="customer_details"

    )
