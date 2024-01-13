import mysql.connector


con=mysql.connector.connect(host="localhost",user="root",password="12345",db="python_db")

# cur=con.cursor()
# cur.execute("create table customers (id int auto_increment primary key,c_name varchar(20),c_number int unique,bill_number int unique,details varchar(500))")
class database():
  def insert(self,name,number,billnum,details='trichy'):
    cur=con.cursor()
    sql="insert into customers (c_name,c_number,bill_number,details)values(%s,%s,%s,%s);"
    user=(name,number,billnum,details)
    cur.execute(sql,user)
    con.commit()
    print("data inserted")

  def select(self):
    cur = con.cursor()
    sql = "select * from customers"
    cur.execute(sql)
    rows = cur.fetchall()
    return rows
  def select_cus(self,c_number):
    cur = con.cursor()
    sql = "select * from customers where c_number=%s;"
    user=(c_number,)
    cur.execute(sql,user)
    rows = cur.fetchall()
    return rows


