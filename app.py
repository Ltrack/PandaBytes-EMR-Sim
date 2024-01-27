# %%
from flask import Flask, render_template, request, url_for, redirect, session, jsonify
from backend.auth import auth, User, users, login_manager
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

import base64
from io import BytesIO
import json
from backend.graph import vitals_graph_grid_plotly
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.register_blueprint(auth)

# Initialize the LoginManager
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"


# User class for Flask-Login
class User(UserMixin):
    def __init__(self, id):
        self.id = id


# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    if user_id not in users:
        return None
    user = User(user_id)
    return user


patient_data_file = os.getenv("PATIENT_DATA_FILE")

patients = None


# read patients from json
def load_patients():
    global patients
    with open(patient_data_file) as json_file:
        patients = json.load(json_file)
    return patients


load_patients()


def get_note_by_id(mrn, encounter, note_id):
    for p in patients:
        if p["mrn"] == mrn and p["encounter"] == encounter:
            for n in p["notes"]:
                if n["id"] == note_id:
                    return n
    return None


def get_report_by_id(mrn, encounter, accession):
    for p in patients:
        if p["mrn"] == mrn and p["encounter"] == encounter:
            for n in p["imaging"]:
                if n["accession"] == accession:
                    return n
    return None


def get_patient(mrn, encounter):
    for p in patients:
        if p["mrn"] == mrn and p["encounter"] == encounter:
            return p
    return None


@app.route("/")
@login_required
def index():
    return render_template("summary.html", patient=patients[0])


@app.route("/set_patient/<int:mrn>")
def set_patient(mrn):
    print(f"Setting patient to {mrn}")
    for patient in patients:
        print(patient["mrn"])
        if int(patient["mrn"]) == mrn:
            print(f"Found patient {patient['mrn']}")
            session["current_patient"] = patient
            return jsonify({"success": True, "message": "Patient set successfully"})
    return jsonify({"success": False, "message": "Patient not found"}), 404


@app.route("/summary")
@login_required
def summary():
    current_patient = session.get("current_patient")
    if not current_patient:
        return redirect(url_for("patient_list"))
    plotly_div, html_table = vitals_graph_grid_plotly(current_patient)
    html_table = html_table.replace("dataframe table table-striped", "summary_table")
    html_table = html_table.replace("NaN", "-")
    html_table = html_table.replace("None", "-")
    return render_template(
        "summary.html",
        patient=current_patient,
        vitals_graph=plotly_div,
        vitals_table=html_table,
    )


@app.route("/labs")
@login_required
def labs():
    current_patient = session.get("current_patient")
    if not current_patient:
        return redirect(url_for("patient_list"))
    plotly_div, html_table = vitals_graph_grid_plotly(current_patient)
    print(html_table)
    html_table = html_table.replace("dataframe table table-striped", "labs_table")
    html_table = html_table.replace("NaN", "-")
    html_table = html_table.replace("None", "-")
    return render_template(
        "labs.html",
        patient=current_patient,
        vitals_graph=plotly_div,
        labs_table=html_table,
    )


@app.route("/patient-list")
@login_required
def patient_list():
    load_patients()
    return render_template("patient_list.html", patients=patients)


@app.route("/imaging")
@login_required
def imaging():
    current_patient = session.get("current_patient")
    return render_template("imaging.html", patient=current_patient)


@app.route("/imaging-", methods=["POST"])
@login_required
def open_report():
    mrn = request.form.get("mrn")
    encounter = request.form.get("encounter")
    accession = request.form.get("accession")
    print(mrn, encounter, accession)
    patient = get_patient(mrn, encounter)
    report = get_report_by_id(mrn, encounter, int(accession))
    # print(report)
    return render_template("imaging_open_report.html", patient=patient, report=report)


@app.route("/chart-review")
@login_required
def chart_review():
    current_patient = session.get("current_patient")
    return render_template("chart_review.html", patient=current_patient)


@app.route("/chart-review-", methods=["POST"])
@login_required
def open_note():
    mrn = request.form.get("mrn")
    encounter = request.form.get("encounter")
    note_id = request.form.get("note_id")
    print(mrn, encounter, note_id)
    patient = get_patient(mrn, encounter)
    note = get_note_by_id(mrn, encounter, int(note_id))
    print(note)
    return render_template("chart_review_open_note.html", patient=patient, note=note)


if __name__ == "__main__":
    app.run(debug=True)
    # vitals_graph(patients[0])


# %%
