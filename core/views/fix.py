from flask import Blueprint, render_template,g

bp = Blueprint('fix', __name__, url_prefix='/fix')

@bp.route("/")
def fix():

    return render_template("article.html")
