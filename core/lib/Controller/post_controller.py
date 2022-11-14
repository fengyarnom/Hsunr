import time
from ..Db.PostModle import PostModle
from ..Db.Db import select_table
from .tag_controller import tag_delete
def post_insert(data):
    post = {
        'pid': time.strftime("%Y%m%d%H%M%S", time.localtime()),
        'title': data['title'],
        'content': data['content'],
        'tags': data['tags'],
        'author': 'Yarnom',
        'create_date': time.strftime("%Y-%m-%d", time.localtime()),
        'views': 0,
        'visible': int(data['visible']),
        'is_top': int(data['is_top'])
    }
    post_modle = PostModle()
    post_modle.insert(post)
    return post['pid']
def post_update(data):
    post = {
        'pid': data['pid'],
        'title': data['title'],
        'content': data['content'],
        'tags': data['tags'],
        'views': 0,
        'visible': int(data['visible']),
        'is_top': int(data['is_top'])
    }
    post_modle = PostModle()
    post_modle.updateByPid(post)

def post_get_count():
    post_modle = PostModle()
    post_modle.getCount()

def post_delete(pid):
    post = select_table(modle=PostModle(),condition="pid='{}'".format(pid),limit=1)
    for item in post['tags'].split(';'):
        tag_delete(condition="name='" + item + "'")
    PostModle().deletePost(pid)
