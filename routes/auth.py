from flask import Blueprint, render_template, request, redirect, flash, session, url_for
import bcrypt
from database.connection import connection

auth = Blueprint("auth", __name__)


# ==========================
# LOGIN
# ==========================
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        if user and bcrypt.checkpw(
    password.encode("utf-8"),
    user["password"].encode("utf-8")
):

            session["user_id"] = user["id"]
            session["fullname"] = user["fullname"]
            session["email"] = user["email"]

            flash("Login Successful!", "success")

            return redirect(url_for("generator.generate"))

        flash("Invalid Email or Password.", "danger")

    return render_template("login.html")


# ==========================
# REGISTER
# ==========================
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cursor.fetchone()

        if user:
            flash("Email already registered.", "danger")
            return redirect("/register")

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        cursor.execute(
            """
            INSERT INTO users(fullname,email,password)
            VALUES(%s,%s,%s)
            """,
            (
                fullname,
                email,
                hashed_password
            )
        )

        connection.commit()

        flash("Registration Successful. Please Login.", "success")

        return redirect("/login")

    return render_template("register.html")


# ==========================
# LOGOUT
# ==========================
@auth.route("/logout")
def logout():

    session.clear()

    flash("Logged Out Successfully.", "success")

    return redirect("/login")