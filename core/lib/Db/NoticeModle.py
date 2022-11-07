from .Db import DB_CTRL
class Notice(DB_CTRL):
    def __init__(self):
        self.conn = super().connectDatabase()
        self.cursor = self.conn.cursor()
        self.format = ['pid','title','content','create_date','visible']
    def init_table(self):
        sql = ("CREATE TABLE NOTICE("
           "pid         CHAR(50)  PRIMARY KEY       NOT NULL,"
           "title       CHAR(100)                   NOT NULL,"
           "content     TEXT                        NOT NULL,"
           "create_date CHAR(50)                    NOT NULL,"
           "visible     INT                         NOT NULL);"    
           )

        self.cursor.execute(sql)
        self.conn.commit()
    
    def insert(self,notice):
        sql = ("INSERT INTO NOTICE VALUES ("
               "'{pid}','{title}','{content}','{create_date}',{visible})".format(
            pid=notice['pid'],
            title=notice['title'],
            content=notice['content'],
            create_date=notice['create_date'],
            visible=notice['visible'],     
            ))
        self.cursor.execute(sql)
        self.conn.commit()

    def updateByPid(self,notice):
        sql=("UPDATE NOTICE SET title='{title}',content='{content}' WHERE pid='{pid}';".format(
            pid=notice['pid'],
            title=notice['title'],
            content=notice['content']
            ))
        self.cursor.execute(sql)
        self.conn.commit()
    
    def getCount(self):
        sql = "select count(*) from NOTICE"
        self.cursor.execute(sql)
        count = self.cursor.fetchone()
        return count[0]
    
    def deleteNoticeByPid(self,condition):
        sql=("UPDATE NOTICE SET visible=0 WHERE {condition}".format(
            condition=condition
            
            ))
        self.cursor.execute(sql)
        self.conn.commit()