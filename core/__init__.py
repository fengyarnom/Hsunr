import datetime
import os


import click
from flask import Flask,session
from .views import index, article,login,admin
from .lib.Config import check_config
from .lib.Db import check_database,init_db
from flask_session import Session
@click.group()
def run():
    click.echo(" * 正在启动应用：")
    pass

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Yarnom'
    app.config.from_object(__name__)
    # 注册蓝图
    app.register_blueprint(index.bp)
    app.register_blueprint(article.bp)
    app.register_blueprint(admin.bp)

    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = os.urandom(24)
    Session(app)
    return app

@click.command()
@click.option("--config-file", help="指定配置文件")
def run_app(config_file):
    app = create_app()


    check_config(config_file)
    check_database(config_file)
    click.echo(" * 启动成功：")

    app.run(debug=True)

# 注册命令
run.add_command(run_app)
run.add_command(init_db)




