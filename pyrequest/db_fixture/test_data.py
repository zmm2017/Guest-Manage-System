from mysql_db import DB 

#创建测试数据
datas={
	"sign_event":[
		{'id':1,"name":'mi 1',"address":'add-mi 1','lim':110,'status':1,'start_time':'2018-05-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':2,"name":'mi 2',"address":'add-mi 2','lim':120,'status':0,'start_time':'2018-05-17 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':3,"name":'mi 3',"address":'add-mi 3','lim':130,'status':1,'start_time':'2018-05-18 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':4,"name":'mi 4',"address":'add-mi 4','lim':140,'status':0,'start_time':'2018-05-19 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':5,"name":'mi 5',"address":'add-mi 5','lim':150,'status':1,'start_time':'2018-06-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':6,"name":'mi 6',"address":'add-mi 6','lim':160,'status':0,'start_time':'2018-06-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':7,"name":'mi 7',"address":'add-mi 7','lim':170,'status':1,'start_time':'2018-07-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':8,"name":'mi 8',"address":'add-mi 8','lim':180,'status':0,'start_time':'2018-07-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':9,"name":'mi 9',"address":'add-mi 9','lim':190,'status':1,'start_time':'2018-07-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':10,"name":'mi 10',"address":'add-mi 10','lim':210,'status':0,'start_time':'2018-08-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':11,"name":'mi 11',"address":'add-mi 11','lim':220,'status':1,'start_time':'2018-08-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':12,"name":'mi 12',"address":'add-mi 12','lim':230,'status':0,'start_time':'2018-09-16 10:00:00','create_time':'2018-02-09 18:00:00'},
		{'id':13,"name":'mi 13',"address":'add-mi 13','lim':240,'status':1,'start_time':'2018-09-16 10:00:00','create_time':'2018-02-09 18:00:00'},
	],
	"sign_guest":[
		{'id':1,'realname':'rn1','phone':'139 0000 0001','email':'rn1@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':2,'realname':'rn2','phone':'139 0000 0002','email':'rn2@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':3,'realname':'rn3','phone':'139 0000 0003','email':'rn3@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':4,'realname':'rn4','phone':'139 0000 0004','email':'rn4@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':5,'realname':'rn5','phone':'139 0000 0005','email':'rn5@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':6,'realname':'rn6','phone':'139 0000 0006','email':'rn6@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':7,'realname':'rn7','phone':'139 0000 0007','email':'rn7@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':1},
		{'id':8,'realname':'rn8','phone':'139 0000 0008','email':'rn8@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
		{'id':9,'realname':'rn9','phone':'139 0000 0009','email':'rn9@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
		{'id':10,'realname':'rn10','phone':'139 0000 00010','email':'rn10@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
		{'id':11,'realname':'rn11','phone':'139 0000 00011','email':'rn11@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
		{'id':12,'realname':'rn12','phone':'139 0000 00012','email':'rn12@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
		{'id':13,'realname':'rn13','phone':'139 0000 00013','email':'rn13@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
		{'id':14,'realname':'rn14','phone':'139 0000 00014','email':'rn14@test.com','sign':0,'create_time':'2018-02-09 18:00:00','event_id':2},
	]
}

#将测试数据插入到数据库中
def init_data():
	db=DB()
	for table,data in datas.items():
		db.clear(table)
		for d in data:
			db.insert(table,d)
	db.close()

if __name__=="__main__":
	init_data()
	print("Insert all the data to DB successfully. Congratulations!")