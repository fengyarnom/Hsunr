from .Db import get_db
class UserModle():
    def __init__(self,init=False):
        self.conn = get_db()
        self.cursor = self.conn.cursor()
        self.format = ['id','username',"password","registration_time","permission"]
        self.table_name = "USER"

        if init is True:
            self.init_table()
    def init_table(self):
        sql = ("CREATE TABLE USER("
           "id                  CHAR(50)  PRIMARY KEY       NOT NULL,"
           "username            CHAR(100)                   NOT NULL,"
           "password            CHAR(50)                    NOT NULL,"
           "registration_time   CHAR(50)                    NOT NULL,"
           "permission          INT                         NOT NULL);")

        self.cursor.execute(sql)
        self.conn.commit()
        print(" - 已初始化 USER 表")
    def insert(self,user):
        sql = ("INSERT INTO USER VALUES ('{id}','{username}','{password}','{registration_time}',{permission})".format(
            id=user['id'],
            username=user['username'],
            password=user['password'],
            registration_time=user['registration_time'],
            permission=user['permission']))
        self.cursor.execute(sql)
        self.conn.commit()

    def select_fetchall(self,condition=""):
        if condition is not None:
            condition = " WHERE "+condition
            
        sql = "SELECT * FROM USER" + condition
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def delete_table(self):
        sql = ("DROP TABLE USER")

        self.cursor.execute(sql)
        self.conn.commit()