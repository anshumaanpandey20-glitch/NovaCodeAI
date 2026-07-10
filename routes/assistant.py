from flask import Blueprint, render_template, request
from services.chat_service import chat_with_ai

assistant = Blueprint("assistant", __name__)


@assistant.route("/assistant", methods=["GET", "POST"])
def index():

    reply = ""

    if request.method == "POST":

        message = request.form.get("message")

        reply = chat_with_ai(message)

    return render_template(
        "assistant.html",
        reply=reply
    )