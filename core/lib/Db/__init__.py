import os
import click
from flask import json

class DB_CTRL:
    @click.command()
    @click.option('--create-database',help='create [database_name] database')
    def check_database(self,create_database=None,config_file=None,db_name=None):
        if config_file is None:
            config_file = "config.json"

        if db_name is None:
            db_name = "hsunr"

        # 检测数据库是否存在
        if not self.is_db_file_exists(config_file,db_name):
            if create_database is not None:
                username = input("请输入管理员名字：")
                password = input("请输入管理员密码：")
                click.echo('初始化数据库成功。')
            else:
                click.echo('数据库未创建或丢失，无法启动服务器。请按照下面类似的操作：\napp.py --create-database [database name]')

    def is_db_file_exists(config_file,db_name):
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)
            if "db_name" in config:
                if os.path.exists(config['db_name'] + ".db"):
                    return True
                else:
                    return False
            else:
                return False
