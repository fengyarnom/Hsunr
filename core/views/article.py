from flask import Blueprint, render_template

bp = Blueprint('article', __name__, url_prefix='/a')

@bp.route("/")
def article():
    return render_template("header.html")

