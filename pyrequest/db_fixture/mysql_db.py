from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser  #configparser是一个模块，提供了ConfigParser class

#=====================读取db_config.ini文件配置==================================================
base_dir=str(os.path.dirname(os.path.abspath(__file__)))
#print(base_dir)
base_dir=base_dir.replace('\\','/')
#print(base_dir)
file_path=base_dir +'/db_config.ini'
#print(file_path)

cf=cparser.ConfigParser() #实例化
cf.read(file_path) #读取配置文件

host=cf.get("mysqlconf","host") #mysqlconf是ini配置文件中的一个section， host是这个section里的一个key
port=cf.get("mysqlconf","port")
user=cf.get("mysqlconf","user")
password=cf.get("mysqlconf","password")
db=cf.get("mysqlconf","db_name")

#======================封装MySQL基本操作==========================================================
class DB:
	def __init__(self):
		#连接数据库
		try:
			self.conn=connect(host=host,
				port=int(port),
				user=user,
				password=password,
				db=db,
				charset="utf8mb4",
				cursorclass=cursors.DictCursor)
		except OperationalError as e:
			print("Mysql Error %d %s" % (e.args[0],e.args[1]))

	#清楚数据
	def clear(self,table_name):
		# real_sql="truncate table" + table_name + ";"
		print("table name is:"+table_name)
		real_sql="delete from " + table_name + ";" #待执行的sql语句
		print(real_sql)
		with self.conn.cursor() as cursor: #实例化cursor对象，通过self.conn对象获取到cursor对象，这个对象的作用就是游标指针，执行SQL语句
			cursor.execute("SET FOREIGN_KEY_CHECKS=0;") #执行sql语句，禁止外键检测
			print("foreign")
			print("foreign")
			print("foreign")
			cursor.execute(real_sql) #执行删除数据（清空表）SQL语句
		self.conn.commit()



if __name__=="__main__":
	db=DB()
	db.clear('sign_event')