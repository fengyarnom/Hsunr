from .Db import DB_CTRL
class Tag(DB_CTRL):
    def __init__(self):
        self.conn = super().connectDatabase()
        self.cursor = self.conn.cursor()
        self.format = ['pid','name','count']
    def init_table(self):
        sql = ("CREATE TABLE TAG("
           "pid         CHAR(50)  PRIMARY KEY       NOT NULL,"
           "name        CHAR(100)                   NOT NULL,"
           "count       INT                         NOT NULL);"        
           )

        self.cursor.execute(sql)
        self.conn.commit()
    
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