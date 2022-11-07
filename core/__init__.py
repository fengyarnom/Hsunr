from flask import Flask,render_template,session
from .views import index, article ,fix
from .lib.Config import check_config
from .lib.Db import check_database
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Yarnom'



    # 注册蓝图
    app.register_blueprint(index.bp)
    app.register_blueprint(article.bp)
    app.register_blueprint(fix.bp)
    return app

def init_app(config_file=None,db_name=None):
    check_config(config_file)
    check_database(db_name)




