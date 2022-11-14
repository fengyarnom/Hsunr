from ..Config import get_config
import sqlite3
def get_db(config_file=None):
    config = get_config(config_file)
    conn = sqlite3.connect(config['db_name'] + ".db")

    return conn


def select_table(col='*',modle=None, condition="", order_by="", limit=0, offset=0):
    conn = get_db()
    cursor = conn.cursor()

    if modle is None:
        return False
    else:
        sql = "SELECT {col} FROM {table_name}".format(col=','.join(col),table_name=modle.table_name)
        if condition != "":
            sql += " WHERE " + condition

        if order_by != "":
            sql += " ORDER BY " + order_by

        if limit != 0:
            sql += " LIMIT " + str(limit)
            if offset != 0:
                sql += " Offset " + str(offset)
        print(sql)
        cursor.execute(sql)
        rows = cursor.fetchall()

        if modle:
            return_data = []
            if col != '*':
                for item in rows:
                    return_data.append(dict(zip(col, item)))
            else:
                for item in rows:
                    return_data.append(dict(zip(modle.format, item)))
            rows = return_data

        if len(rows) == 0:
            return rows
        elif len(rows) == 1:
            if limit==1:
                return rows[0]
            else:
                return rows
        else:
            return rows