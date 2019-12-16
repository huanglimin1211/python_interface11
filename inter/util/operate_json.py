import json
import os

class OperateJson(object):
	"""docstring for OperateJson"""
	def __init__(self,filepath=None):
		if filepath:
			self.filepath=filepath
		else:
			self.filepath='../data_config/user11.json'
		self.file = open(self.filepath)
		
	def get_json(self):
		res=json.load(self.file)#load,从字符串类型转变成Python数据类型dict
		print(res)
		return res


	def get_data(self,search):
		self.res=self.get_json()
		print(self.res)
		data=self.res[search]
		print(data)
		return data


if __name__ == '__main__':
	filepath=os.path.abspath("../data_config/user11.json")
	operate=OperateJson(filepath)
	res=operate.get_json()
	print(res["user"])
	operate.get_data("user")


