import unittest
import requests
#from models import Event,Guest

class AddEventTest(unittest.TestCase):
	def setUp(self):
		self.url="http://127.0.0.1/api/add_event/"
	
	#测试传递空参数
	def test_bad_parameter(self):
		r=requests.post(self.url)
		result=r.json()
		self.assertEqual(result['message'],'parameter error')
		self.assertEqual(result['status'],10021)

	#测试id重复
	def test_duplicate_id(self):
		payload={'eid':7,'name':'mi 14','address':'add-mi 14','lim':200,'status':1,'start_time':'2018-06-01 10:00:00','create_time':'2018-02-11 17:00:00'}
		r=requests.post(self.url, data=payload)
		result=r.json()
		self.assertEqual(result['message'],'event id already exists')
		self.assertEqual(result['status'],10022)

	#测试name重复
	def test_duplicate_name(self):
		payload={'eid':140,'name':'mi 7','address':'add-mi 14','lim':200,'status':1,'start_time':'2018-06-01 10:00:00','create_time':'2018-02-11 17:00:00'}
		r=requests.post(self.url,data=payload)
		result=r.json()
		self.assertEqual(result['message'],'event name already exists')
		self.assertEqual(result['status'],10023)

	#测试正确传递参数的执行结果
	def test_add_event(self):
		payload={'eid':18,'name':'mi 18','address':'add-mi 18','lim':200,'start_time':'2018-06-01 10:00:00','create_time':'2018-02-11 17:00:00'}
		r=requests.post(self.url, data=payload)
		result=r.json()
		self.assertEqual(result['message'],'add event success')
		self.assertEqual(result['status'],200)

	#测试时间格式错误
	def test_wrong_format_time(self):
		payload={'eid':19,'name':'mi 19','address':'add-mi 19','lim':200,'start_time':'2018.06.08 10:00','create_time':'2018-02-11 17:00:00'}
		r=requests.post(self.url, data=payload)
		result=r.json()
		self.assertEqual(result['message'],'start_time format error')
		self.assertEqual(result['status'],10024)



if __name__=="__main__":
	unittest.main()