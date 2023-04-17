from flask import Flask, render_template
from flask_restx import Api

from project.setup_db import db
from project.views import documents_ns

api = Api()


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(documents_ns)

    return app
