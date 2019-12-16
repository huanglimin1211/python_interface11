# coding= utf-8
import os, sys, json,requests
from time import sleep

DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR_BASE)
from run_method import RunMethod
from getdata.get_data import GetData
from util.commom_util import Common_Util
from util.connect_db import ConnectDB
from smtp_email import Send_Email


class RunTest(object):
	def __init__(self, filepath, index):
		self.runmethod = RunMethod()
		self.data = GetData(filepath, index)
		self.commom_util = Common_Util()
		self.db = ConnectDB()
	
	# 登陆获取token
	def login(self):
		url = 'http://dfc.dasouche.net/rest/account/login?loginName=17816104011&password=souche2015'
		# 获取session对象
		s = requests.session()
		res = self.runmethod.run_method('post', url, headers=None, data=None)
		return s
		

	
	
	def run_test(self):
		pass_list = [1, 2, 3, 4]
		fail_list = [5]
		
		s = self.login()
		cases = self.data.get_case_lines()
		for i in range(2, cases):
			sleep(1)
			isrun = self.data.get_isrun(i)
			url = self.data.get_url_value(i)
			method = self.data.get_runmethod(i)
			expect = self.data.get_expect_value(i)
			# data = self.data.get_data_forjson(i)
			json = self.data.get_data_forjson()
			res = self.data.get_request_data(i)
			data = json[res]
			expect_data = self.db.search_one(expect)
			expect_string0 = expect_data.__str__()  # 将tuple类型转换为str类型
			expect_string = expect_string0.split("'", 1)[1].split("'", 1)[0]
			print(expect_string0)
			# header = {
			# 	"_security_token": token
			# }
			# print("data的数据为：%s"  %data)
			sleep(1)
			if isrun == "yes":
				res = self.runmethod.run_method(method, url, headers=None, data=None)
				print(res)
				# print(type(res))
				result = self.commom_util.is_contain(expect_string, res)
				if result == True:
					self.data.write_value(i, "pass")
					pass_list.append(i)
				else:
					self.data.write_value(i, "fail")
			# fail_list.append(12)
			else:
				return None
		
		pass_num = len(pass_list)
		fail_num = len(fail_list)
		total_num = pass_num + fail_num
		pass_result = "%.2f%%" % (pass_num / total_num)
		fail_result = "%.2f%%" % (fail_num / total_num)
		content = "测试通过的用例个数为%s，失败的个数为%s，通过率%s，失败率%s" % (pass_num, fail_num, pass_result, fail_result)
		url = os.path.abspath("../report/2019-08-03Test.html")


if __name__ == '__main__':
	filepath = os.path.abspath('../data_config/case1.xls')
	run = RunTest(filepath, 0)
	res = run.login()
	print(res)
