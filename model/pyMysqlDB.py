import pymysql.cursors
import pymysql
# Connect to the database

class myDB(object):
    def __init__(self):
        pass
    def connect_function(self,funcName):
        connect = pymysql.Connect(host='172.168.101.85', port=3306, user='ces', passwd='WY68Yud', db='yws',
                                  charset='utf8mb4')
        cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # cursor.callproc('proInsert', args = ('2'))
            # cursor.execute("select  @proInsert")

            sql= 'select   '+ funcName
            cursor.execute(sql)
            row_1 = cursor.fetchone()
            returnNum=row_1[funcName]
            connect.commit()
            cursor.close()
        finally:
            connect.close()
        return returnNum
if __name__=='__main__':
    myDB.connect_function(myDB,'func_autoInsertStudent(2)')
