from flask import Blueprint, render_template
from core.lib.Db.Db import select_table
from core.lib.Db.PostModle import PostModle
from core.lib.Db.TagModle import TagModle
bp = Blueprint('index', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/article")
def index():

    posts = select_table(
        modle=PostModle(),
        limit=12,
        order_by='pid desc,create_date desc',
        condition="tags != '日记' and tags != '公告' and visible=1"
    )

    tags = select_table(
        modle=TagModle(),
        limit=15,
        order_by='count desc',
    )

    notice = select_table(
        modle=PostModle(),
        limit=3,
        condition="tags == '公告' and visible=1",
        order_by='pid desc',
    )
    return render_template("article.html",posts=posts,tags=tags,notice=notice)

@bp.route("/daily")
def daily():

    return render_template("daily.html")