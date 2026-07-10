from flask import Blueprint, render_template, request, session, redirect, flash
from database.connection import connection
from services.ai_service import generate_code

generator = Blueprint("generator", __name__)


@generator.route("/generator", methods=["GET", "POST"])
def generate():

    if "user_id" not in session:
        flash("Please login first.", "danger")
        return redirect("/login")

    generated_code = ""
    language = "Python"
    framework = "None"

    if request.method == "POST":

        print(request.form)
        print(request.form.get("language"))
        print(request.form.get("framework"))

        prompt = request.form.get("prompt")
        language = request.form.get("language", "Python")
        framework = request.form.get("framework", "None")

        language = language.lower()
        framework = framework.lower()

        if not prompt or prompt.strip() == "":
            flash("Please enter a prompt.", "danger")
            return redirect("/generator")

        generated_code = generate_code(
            prompt,
            language,
            framework
        )

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO generations
            (
                user_id,
                prompt,
                language,
                framework,
                generated_code
            )
            VALUES(%s,%s,%s,%s,%s)
            """,
            (
                session["user_id"],
                prompt,
                language,
                framework,
                generated_code
            )
        )

        connection.commit()

        flash("Code generated successfully!", "success")

    return render_template(
        "generator.html",
        generated_code=generated_code,
        language=language.lower()
    )