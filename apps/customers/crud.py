@blueprint.route("/Patient_Info/", methods=["GET", "POST"])
@login_required
def patient_info_page():
     if request.method == "GET":
         return render_template("ID.html", query=patient_ID.query.all())

     if not current_user.is_authenticated:
         return redirect(url_for('index'))
     ID = patient_ID(mrn=request.form["mrns"])