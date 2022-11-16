import time

from flask import Blueprint, render_template
from core.lib.Db.Db import select_table
from core.lib.Db.PostModle import PostModle
from core.lib.Db.TagModle import TagModle
bp = Blueprint('index', __name__, url_prefix='/')

@bp.route("/")
@bp.route("/<string:view>")
def index(view="article"):
    if view == "daily":
        condition = "tags == '日记'"
    else:
        condition = "tags != '日记' and tags != '公告'"
    top_posts = select_table(
        modle=PostModle(),
        limit=5,
        order_by='pid desc,create_date desc',
        condition=condition+" and is_top=1"
    )
    posts = select_table(
        modle=PostModle(),
        limit=5,
        order_by='pid desc,create_date desc',
        condition=condition+" and is_top=0"
    )


    recent_posts = select_table(
        modle=PostModle(),
        limit=15,
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
    return render_template("article.html",top_posts=top_posts,posts=posts,recent_posts=recent_posts,tags=tags,notice=notice)


@bp.route("/archive/<path:order_by>")
def archive(order_by="date"):
    archive_list = list()
    if "date" in order_by :
        for year in range(int(time.strftime("%Y", time.localtime())),2019, -1):
            posts = select_table(
                col=['title','create_date'],
                modle=PostModle(),
                condition="tags!='日记' and tags!='通告' and create_date like '{}%'".format(str(year)),
                order_by="create_date desc,pid desc"
            )
            if len(posts) != 0:
                archive_list.append({
                    "year":year,
                    "data":posts
                })
    elif "tag" in order_by:
        tag_name = order_by.split("/")[1]
        print(order_by.split("/"))
        posts = select_table(
            col=['title', 'create_date'],
            modle=PostModle(),
            condition="tags!='日记' and tags!='通告' and tags = '{}'".format(tag_name),
            order_by="create_date desc,pid desc"
        )
        archive_list.append({
            "year": tag_name,
            "data": posts
        })
    return render_template("archive.html",archive_list=archive_list)