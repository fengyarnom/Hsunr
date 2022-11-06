from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/article")
def index(name=None):

    return render_template("article.html",name=name)

@bp.route("/daily")
def daily(name=None):

    return render_template("daily.html",name=name)