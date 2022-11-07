from flask import Blueprint, render_template
from core.lib.Db import get_db
bp = Blueprint('index', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/article")
def index():
    print(get_db)
    return render_template("article.html")

@bp.route("/daily")
def daily():

    return render_template("daily.html")