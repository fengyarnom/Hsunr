import time

from flask import Blueprint, render_template,request
from ..lib.Controller.post_controller import post_insert,post_update,post_delete
from ..lib.Controller.tag_controller import tag_insert,tag_update
from ..lib.Db.PostModle import PostModle
from ..lib.Db.Db import select_table
from ..lib.ResultBody import ResultCode,res2json
bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route("/")
@bp.route("/<string:view>/page/<int:page>", methods=['POST','GET'])
def article(view="aritcle",page=1):
    page -= 1

    if view == "daily":
        condition = "tags == '日记'"
    elif view == "notice":
        condition = "tags == '公告'"
    else:
        condition = "tags != '日记' and tags != '公告'"
    post = select_table(
        modle=PostModle(),
        condition=condition,
        order_by='pid desc,create_date desc',
        limit=10,
        offset=page*10
    )
    post_count = select_table(
        col=['count(*)'],
        modle=PostModle(),
        condition="tags != '日记' and tags != '公告'",
        limit=1
    )['count(*)']

    print(post_count)

    daily_count = select_table(
        col=['count(*)'],
        modle=PostModle(),
        condition="tags == '日记'",
        limit=1
    )['count(*)']

    notice_count = select_table(
        col=['count(*)'],
        modle=PostModle(),
        condition="tags == '公告'",
        limit=1
    )['count(*)']
    print(post)

    return render_template(
        "admin_article.html",
        post=post,
        post_count=post_count,
        daily_count=daily_count,
        notice_count=notice_count
    )

@bp.route("/editor/", methods=['POST','GET'])
@bp.route("/editor/<string:post_pid>", methods=['POST','GET'])
def editor(post_pid=None):
    post = None
    if request.method == "POST":
        request_data = request.json
        if request_data['pid'] == '':
            pid = post_insert(request_data)
            tag_insert(request_data['tags'])
            return res2json(ResultCode.SUCCESS_POST_CREATED,pid)
        else:
            old_post = select_table(modle=PostModle(), condition="pid='{}'".format(request_data['pid']),limit=1)
            # 先更新 TAG,再更新 POST
            tag_update(old_post,request_data)
            post_update(request_data)
            return res2json(ResultCode.SUCCESS_POST_MODIFIED,"")

    if post_pid is not None:
        post = select_table(modle=PostModle(), condition="pid='{}'".format(post_pid),limit=1)
        print(post)
    return render_template("editor.html",post=post)


@bp.route("/delete/<string:post_pid>", methods=['POST'])
def delete(post_pid):
    if request.method == "POST":
        request_data = request.json
        print(request_data)
        post_delete(request_data['pid'])
        return res2json(ResultCode.SUCCESS_POST_DELETE,"")