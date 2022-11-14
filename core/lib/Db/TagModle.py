from .Db import get_db
class TagModle():
    def __init__(self,init=False):
        self.conn = get_db()
        self.cursor = self.conn.cursor()
        self.format = ['pid','name','count']
        self.table_name = "TAG"
        if init is True:
            self.init_table()
    def init_table(self):
        sql = ("CREATE TABLE TAG("
           "pid         CHAR(50)  PRIMARY KEY       NOT NULL,"
           "name        CHAR(100)                   NOT NULL,"
           "count       INT                         NOT NULL);"        
           )

        self.cursor.execute(sql)
        self.conn.commit()
        print(" - 已初始化 Tag 表")
    def insert(self,tag):
        sql = ("INSERT INTO TAG VALUES ("
               "'{pid}','{name}',{count})".format(
            pid=tag['pid'],
            name=tag['name'],
            count=tag['count'],     
            ))
        self.cursor.execute(sql)
        self.conn.commit()

    def updateByPid(self,tag):
        sql=("UPDATE TAG SET count='{count}' WHERE pid='{pid}';".format(
            pid=tag['pid'],
            count=tag['count']
            ))
        self.cursor.execute(sql)
        self.conn.commit()
    def getCount(self):
        sql = "select count(*) from TAG"
        self.cursor.execute(sql)
        count = self.cursor.fetchone()
        return count[0]
    
    def deleteTagByPid(self,pid):
        sql = "delete from TAG where pid='"+pid+"'"
        self.cursor.execute(sql)
        self.conn.commit()