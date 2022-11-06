from flask import Flask, render_template, url_for, Blueprint
from .views import index,article

app = Flask(__name__)
def create_app():

    app.register_blueprint(index.bp)
    app.register_blueprint(article.bp)
    return app


