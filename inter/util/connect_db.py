#coding=utf-8
import  pymysql

class  ConnectDB():
    def __init__(self):
        self.con=pymysql.connect('dev.database003.scsite.net','root','dpjA8Z6XPXbvos','souche_detect')
        self.cursor=self.con.cursor()

    def search_one(self,sql):
        self.cursor.execute(sql)
        data=self.cursor.fetchone()
        return data
    def close_db(self):
        self.con.close()


if __name__ == '__main__':
    db1=ConnectDB()
    data=db1.search_one("select check_result_msg from report_cyp_info where car_id='f44d0a7c964643dc925cc35d6930c7a9'")
    print("数据库返回结果为 %s"   %data)
    print(type(data))
    db1.close_db()

