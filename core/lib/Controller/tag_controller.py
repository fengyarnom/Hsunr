import time

from ..Db.Db import select_table
from ..Db.TagModle import TagModle
def tag_insert(tags):
    tag_modle = TagModle()
    print(tags)
    for item in tags.split(';'):
        tag_row = select_table(modle=TagModle(),limit=1,condition="name='{}'".format(item))
        if len(tag_row) == 0:
            tag = {
                'pid': str(time.time()),
                'name': item,
                'count': 1
            }
            tag_modle.insert(tag)
        else:
            print(tag_row)
            tag = {
                'pid': tag_row['pid'],
                'name': tag_row['name'],
                'count': tag_row['count'] + 1
            }
            tag_modle.updateByPid(tag)

def tag_update(old_post,new_post):

    for item in old_post['tags'].split(';'):
        tag_delete(condition="name='" + item + "'")
    tag_insert(new_post['tags'])

def tag_delete(condition):
    selected_tag = select_table(modle=TagModle(),condition=condition,limit=1)
    if (len(selected_tag) != 0):
        tag = {
            'pid': selected_tag['pid'],
            'name': selected_tag['name'],
            'count': selected_tag['count'] - 1
        }
        if tag['count'] <= 0:
            TagModle().deleteTagByPid(tag['pid'])
        else:
            TagModle().updateByPid(tag)