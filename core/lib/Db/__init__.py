import os
import sqlite3
import time

import click
from flask import json

from ..Config import update_config_file,get_config
from .Db import get_db
from .UserModle import UserModle
from .PostModle import PostModle
from .TagModle import TagModle

def init_db_confirm(ctx, param, value):
    if value == False:
        exit(0)
@click.command()
@click.option('--yes', is_flag=True,expose_value=False,callback=init_db_confirm,prompt=' * 此操作会摧毁先前可能已存在的数据库，你确定要初始化吗？')
@click.option('--config-file',prompt=' * 请输入配置文件 [默认为空即可]',default="config.json",help='指定配置文件')
@click.option('--database',prompt=' * 请输入数据库名：',default="Hsunr",help='即将要创建的数据库名字')
@click.option('--username',prompt=' * 请输入管理员名字：',default="root",help='设置管理员用户名')
@click.option('--password',prompt=' * 请输入管理员密码：',default="root",hide_input=True,confirmation_prompt="* 请重复管理员密码：",help='设置管理员密码')
def init_db(config_file,database,username,password):
    config = get_config(config_file)
    if 'db_name' in config:
        if os.path.exists(config['db_name'] + ".db"):
            os.remove(config['db_name'] + ".db")

    config = {
        "db_name": database
    }
    admin_user = {
        "id": time.strftime("%Y%m%d%H%M%S", time.localtime()),
        "username": username,
        "password": password,
        "registration_time": time.strftime("%Y-%m-%d", time.localtime()),
        "permission": 0
    }
    update_config_file(config_file, config)

    conn = get_db(config_file)
    UserModle(init=True).insert(admin_user)
    PostModle(init=True)
    TagModle(init=True)

    click.echo(' * 初始化数据库成功,请重新运行程序。')

def check_database(config_file=None):
    if config_file is None:
        config_file = "config.json"

    # 检测数据库是否存在
    if not is_db_file_exists(config_file):
        print   (' * 启动失败')
        print(' * 数据库未创建或丢失，请检查配置文件和数据库文件。如需要初始化数据库，请按照下面类似的操作：app.py --init-db')
        exit(-1)

def is_db_file_exists(config_file):
    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)
        if "db_name" in config:
            if os.path.exists(config['db_name'] + ".db"):
                return True
            else:
                return False
        else:
            return False







