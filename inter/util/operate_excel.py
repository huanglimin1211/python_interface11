#coding=utf-8
import xlrd
import os
from xlutils.copy import copy
class OperateExcel(object):
	def __init__(self, filepath,index):
		self.filepath=filepath
		self.index=index
		self.data=self.get_data()
	# def __init__(self, filepath=None,index=None):
	# 	# if filepath:
	# 	# 	self.filepath=filepath
	# 	# 	self.index=index
	# 	# else:
	# 	# 	self.filepath="./data_config/case1.xls"
	# 	# 	self.index=0
	# 	self.data=self.get_data()
	def get_data(self):	
		book=xlrd.open_workbook(self.filepath)
		print(book.sheet_names())
		sheet=book.sheet_by_index(self.index)
		return sheet
	def get_lines(self):
		nrows=self.data.nrows
		print(nrows)
		return nrows
	def get_cell_value(self,row,col):
		value=self.data.cell(row,col).value
		print(value)
		return value

	def write_data(self,row,col,value):
		read_data=xlrd.open_workbook(self.filepath)
		write_data=copy(read_data)
		sheet=write_data.get_sheet(0)
		sheet.write(row,col,value)
		write_data.save(self.filepath)

if __name__ == '__main__':
	filepath=os.path.abspath("../data_config/case1.xls")
	operate=OperateExcel(filepath,0)
	operate.get_data()
	operate.get_lines()
	operate.get_cell_value(2,3)
	operate.write_data(2,3,'yes')
	operate.get_cell_value(2,3)









