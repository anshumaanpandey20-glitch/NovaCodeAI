from flask import Blueprint, render_template, session, redirect
from database.connection import connection

profile = Blueprint("profile", __name__)


@profile.route("/profile")
def index():

    if "user_id" not in session:
        return redirect("/login")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id,
               fullname,
               email,
               created_at
        FROM users
        WHERE id=%s
        """,
        (session["user_id"],)
    )

    user = cursor.fetchone()

    cursor.execute(
        """
        SELECT COUNT(*) AS total
        FROM generations
        WHERE user_id=%s
        """,
        (session["user_id"],)
    )

    total = cursor.fetchone()["total"]

    return render_template(
        "profile.html",
        user=user,
        total=total
    )