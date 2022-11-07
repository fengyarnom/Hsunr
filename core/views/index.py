from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/article")
def index():
    return render_template("article.html")

@bp.route("/daily")
def daily():

    return render_template("daily.html")