from flask import Blueprint, render_template, session, redirect, request, url_for
from database.connection import connection

history = Blueprint("history", __name__)


@history.route("/history")
def index():
    if "user_id" not in session:
        return redirect("/login")

    search = request.args.get("search", "")
    cursor = connection.cursor()

    if search:
        cursor.execute(
            """
            SELECT
                id,
                prompt,
                generated_code,
                language,
                framework,
                created_at
            FROM generations
            WHERE user_id=%s
            AND (
                prompt LIKE %s
                OR language LIKE %s
                OR framework LIKE %s
            )
            ORDER BY created_at DESC
            """,
            (
                session["user_id"],
                f"%{search}%",
                f"%{search}%",
                f"%{search}%"
            )
        )
    else:
        cursor.execute(
            """
            SELECT
                id,
                prompt,
                generated_code,
                language,
                framework,
                created_at
            FROM generations
            WHERE user_id=%s
            ORDER BY created_at DESC
            """,
            (session["user_id"],)
        )

    history = cursor.fetchall()

    return render_template(
        "history.html",
        history=history,
        search=search
    )


@history.route("/history/delete/<int:id>")
def delete(id):
    if "user_id" not in session:
        return redirect("/login")

    cursor = connection.cursor()
    cursor.execute(
        """
        DELETE FROM generations
        WHERE id=%s
        AND user_id=%s
        """,
        (id, session["user_id"])
    )
    connection.commit()

    return redirect(url_for("history.index"))


@history.route("/history/favorite/<int:id>")
def favorite(id):
    if "user_id" not in session:
        return redirect("/login")

    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE generations
        SET is_favorite = NOT is_favorite
        WHERE id=%s
        AND user_id=%s
        """,
        (id, session["user_id"])
    )
    connection.commit()

    return redirect("/history")