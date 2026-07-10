from flask import Blueprint, render_template, session, redirect
from database.connection import connection

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard")
def index():

    if "user_id" not in session:
        return redirect("/login")

    cursor = connection.cursor()

    # Total generations
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM generations
        WHERE user_id=%s
    """, (session["user_id"],))

    total = cursor.fetchone()["total"]

    # Today's generations
    cursor.execute("""
        SELECT COUNT(*) AS today
        FROM generations
        WHERE user_id=%s
        AND DATE(created_at)=CURDATE()
    """, (session["user_id"],))

    today = cursor.fetchone()["today"]

    # Total languages used
    cursor.execute("""
        SELECT COUNT(DISTINCT language) AS languages
        FROM generations
        WHERE user_id=%s
    """, (session["user_id"],))

    languages = cursor.fetchone()["languages"]

    # Recent activity
    cursor.execute("""
        SELECT prompt, language, created_at
        FROM generations
        WHERE user_id=%s
        ORDER BY created_at DESC
        LIMIT 5
    """, (session["user_id"],))

    recent = cursor.fetchall()

    return render_template(
        "dashboard.html",
        fullname=session["fullname"],
        total=total,
        today=today,
        languages=languages,
        recent=recent
    )