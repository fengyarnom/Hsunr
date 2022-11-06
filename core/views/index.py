from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/a")
def hello_world(name=None):

    return render_template("article.html",name=name)