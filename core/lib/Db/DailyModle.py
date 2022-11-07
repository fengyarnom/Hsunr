from .Db import get_db
class DailyModle():
    def __init__(self,init=False):
        self.conn = get_db()
        self.cursor = self.conn.cursor()
        self.format = ['pid','title','content','create_date']
        if init is True:
            self.init_table()
    def init_table(self):
        sql = ("CREATE TABLE DAILY("
           "pid         CHAR(50)  PRIMARY KEY       NOT NULL,"
           "title       CHAR(100)                   NOT NULL,"
           "content     TEXT                        NOT NULL,"        
           "create_date CHAR(50)                    NOT NULL);" 
           )

        self.cursor.execute(sql)
        self.conn.commit()
        print(" - 已初始化 Daily 表")
    def insert(self,daily):
        sql = ("INSERT INTO DAILY VALUES ("
               "'{pid}','{title}','{content}','{create_date}')".format(
            pid=daily['pid'],
            title=daily['title'],
            content=daily['content'],     
            create_date=daily['create_date'],
            ))
        self.cursor.execute(sql)
        self.conn.commit()

    
    def updateByPid(self,daily):
        sql=("UPDATE DAILY SET title='{title}',content='{content}' WHERE pid='{pid}';".format(
            pid=daily['pid'],
            title=daily['title'],
            content=daily['content']
            ))
        self.cursor.execute(sql)
        self.conn.commit()
    
    def getCount(self):
        sql = "select count(*) from DAILY"
        self.cursor.execute(sql)
        count = self.cursor.fetchone()
        return count[0]
    
    def deleteDailyByPid(self,pid):
        sql = "delete from DAILY where pid="+pid
        self.cursor.execute(sql)
        self.conn.commit()