from routes.home import home
from routes.auth import auth
from routes.generator import generator
from routes.home import home
from routes.auth import auth
from routes.dashboard import dashboard
from routes.generator import generator
from routes.history import history
from routes.profile import profile
from routes.assistant import assistant
from flask import Flask

from config import SECRET_KEY

from database.connection import initialize_database



app = Flask(__name__)

app.secret_key = SECRET_KEY

initialize_database()

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(generator)
app.register_blueprint(history)
app.register_blueprint(profile)
app.register_blueprint(assistant)

if __name__ == "__main__":
    app.run(debug=True)