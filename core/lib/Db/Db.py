from ..Config import get_config
import sqlite3
def get_db(config_file=None):

    config = get_config(config_file)
    conn = sqlite3.connect(config['db_name'] + ".db")

    return conn