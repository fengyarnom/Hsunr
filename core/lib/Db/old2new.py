from .Db import *
from .PostModle import *
from .TagModle import *
conn_old = get_db('config_old.json')
cursor_old = conn_old.cursor()
post_modle = PostModle()
tag_modle = TagModle()



def sqliteEscape(string):
    string = string.replace("'", "''")
    return string

def old2newForPost():
    sql = "select * from POST"
    cursor_old.execute(sql)
    rows = cursor_old.fetchall()

    for item in rows:
        post = {
            'pid': item[0],
            'title': item[1],
            'content': sqliteEscape(item[2]),
            'tags': item[3],
            'author':item[4],
            'create_date':item[5],
            'views':item[6],
            'visible':1,
            'is_top': item[7]
        }
        post_modle.insert(post)
def old2newForDaily():
    sql = "select * from Daily"
    cursor_old.execute(sql)
    rows = cursor_old.fetchall()
    for item in rows:
        post = {
            'pid': item[0],
            'title': item[1],
            'content': sqliteEscape(item[2]),
            'tags': "日记",
            'author': "Yarnom",
            'create_date': item[3],
            'views': 0,
            'visible': 1,
            'is_top': 0,
        }
        print(item)
        post_modle.insert(post)

def old2newForNotice():
    sql = "select * from NOTICE"
    cursor_old.execute(sql)
    rows = cursor_old.fetchall()
    for item in rows:
        post = {
            'pid': item[0],
            'title': item[1],
            'content': sqliteEscape(item[2]),
            'tags': "公告",
            'author': "Yarnom",
            'create_date': item[3],
            'views': 0,
            'visible': item[4],
            'is_top': 0,
        }
        print(item)
        post_modle.insert(post)

def old2newForTag():
    sql = "select * from Tag"
    cursor_old.execute(sql)
    rows = cursor_old.fetchall()
    for item in rows:
        tag = {
            'pid': item[0],
            'name': item[1],
            'count': int(item[2]),
        }
        print(item)
        tag_modle.insert(tag)