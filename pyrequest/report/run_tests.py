##########Please execute this script at pyrequests folder,otherwise some erros will occurs.
import sys,time
import unittest
sys.path.append('./interface')
sys.path.append('./db_fixture')
sys.path.append('./report')
from test_data import init_data
from HTMLTestRunner import HTMLTestRunner


#指定测试用例所在位置
test_dir='./interface'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__=='__main__':
	init_data()   #初始化测试数据库

	now=time.strftime("%Y-%m-%d %H_%M_%S")
	filename="./report/"+now+'_result.html'
	fp=open(filename,'wb')

	runner=HTMLTestRunner(stream=fp,title='Guest Manage System interface Test Report',description='Implementation Example with:')
	runner.run(discover)

	fp.close()