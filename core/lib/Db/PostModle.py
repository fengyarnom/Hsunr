from .Db import DB_CTRL
class Post(DB_CTRL):
    def __init__(self):
        self.conn = super().connectDatabase()
        self.cursor = self.conn.cursor()
        self.format = ['pid','title','content','tags','author','create_date','views','isTop']
    def init_table(self):
        sql = ("CREATE TABLE POST("
           "pid         CHAR(50)  PRIMARY KEY       NOT NULL,"
           "title       CHAR(100)                   NOT NULL,"
           "content     TEXT                        NOT NULL,"
           "tags        TEXT                        NOT NULL,"
           "author      CHAR(100)                   NOT NULL,"
           "create_date CHAR(50)                    NOT NULL," 
           "views       INT                         NOT NULL,"     
           "is_top      INT                         NOT NULL);")

        self.cursor.execute(sql)
        self.conn.commit()

    def insert(self,post):
        sql = ("INSERT INTO Post VALUES ("
               "'{pid}','{title}','{content}','{tags}','{author}','{create_date}',{views},{is_top})".format(
            pid=post['pid'],
            title=post['title'],
            content=post['content'],
            author=post['author'],
            create_date=post['create_date'],
            views=post['views'],
            tags=post['tags'],
            is_top=int(post['is_top'])))
        self.cursor.execute(sql)
        self.conn.commit()

    def select_fetchall(self,condition=""):
        if condition is not None:
                    condition = " WHERE "+condition
        
        sql = "SELECT * FROM POST" + condition
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def select_fetchall_orderBy_date(self):
        sql = "SELECT * FROM POST ORDER BY create_date DESC"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows
    
    def updateByPid(self,post):
        sql=("UPDATE POST SET title='{title}',content='{content}',tags='{tags}',is_top='{is_top}' WHERE pid='{pid}';".format(
            pid=post['pid'],
            title=post['title'],
            content=post['content'],
            tags=post['tags'],
            is_top=int(post['is_top'])
            ))
        self.cursor.execute(sql)
        self.conn.commit()
    
    def getCount(self):
        sql = "select count(*) from POST"
        self.cursor.execute(sql)
        count = self.cursor.fetchone()
        return count[0]
    
    def deletePost(self,pid):
        sql = "delete from POST where pid="+pid
        self.cursor.execute(sql)
        self.conn.commit()