#coding=utf-8
import os
import sys
DIR_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(DIR_BASE)
sys.path.append(DIR_BASE)
from util.operate_excel import OperateExcel
from util.operate_json import OperateJson
import  data_config
 
class GetData():
	def __init__(self,filepath,index):
		self.operate=OperateExcel(filepath,index)
		# self.row=row

	def get_case_lines(self):
		num=self.operate.get_lines()
		return num

	def get_isrun(self,row):
		col=int(data_config.get_run())
		isrun=self.operate.get_cell_value(row,col)
		# isrun=self.operate.get_cell_value(col,row)
		if isrun=="yes":
			return "yes"
		else:
			return "no"

	def get_url_value(self,row):
		col=int(data_config.get_url())
		url=self.operate.get_cell_value(row,col)
		return url

	def get_runmethod(self,row):
		col=int(data_config.get_type())
		method=self.operate.get_cell_value(row,col)
		return method

	def get_id_value(self,row):
		col=data_config.get_id()
		Id=self.operate.get_cell_value(col,row)
		return Id

	def is_header(self,row):
		col=int(data_config.get_header())
		header=self.operate.get_cell_value(row,col)
		if header=="yes":
			return data_config.get_header_value()
		else:
		    return None
	def get_expect_value(self,row):
		col=int(data_config.get_expect())
		exp=self.operate.get_cell_value(row,col)
		return exp

	def get_request_data(self,row):
		col=int(data_config.get_data())
		data=self.operate.get_cell_value(row,col)
		return data
	def get_data_forjson(self):
		operate_json=OperateJson()
		request_data=operate_json.get_json()
		return request_data
	def write_value(self,row,value):
		col=int(data_config.get_result())
		self.operate.write_data(row,col,value)

if __name__ == '__main__':
	filepath=os.path.abspath('../data_config/case1.xls')
	operate=GetData(filepath,0)
	operate.get_runmethod(3)
	operate.get_isrun(3)
	operate.get_url_value(3)
	operate.get_case_lines()
	json=operate.get_data_forjson()
	res=operate.get_request_data(3)
	request_data=json[res]
	print(request_data)
	operate.write_value(2,'WODE')


	
