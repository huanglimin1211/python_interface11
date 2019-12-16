#coding=utf-8
import requests
import os
import json
class RunMethod(object):
	"""docstring for RunMethod"""
	def login(self):
		url = 'http://dfc.dasouche.net/rest/account/login?loginName=17816104011&password=souche2015'
		session=requests.session()
		res = requests.post(url, headers=None, data=None)
		# 将json对象转换为字典dict
		return session
	
	def run_post(self,url,headers=None,data=None):
		session=self.login()
		if headers!=None:
			res=session.post(url,headers,data)#此处必须加json(),否则返回200
			# print(res['code'])
		else:
			res=session.post(url,data)
		return res.json()


	def run_get(self,url,data=None,headers=None):
		if headers!=None:
			res=requests.get(url,headers,data).json()
		else:
			res=requests.get(url,data).json()
		return res
	def run_method(self,method,url,headers,data):
		if method=='post':
			res=self.run_post(url,headers,data)
		else:
			res=self.run_get(url,headers,data)
		return json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)#json编码,从字典变成JSON格式:json.dumps();解决有汉字会被编译成unicode码

if __name__ == '__main__':
	filepath=os.path.abspath('../data_config/case1.xls')
	url = 'http://detection.dev.dasouche.net/jiaxuanreport/jxDetectAction/selectCheckResultMsg.json?carId=35bff94b6b394e5eafb2280b2784fd15'
	header = {
		"Content-Type": "application/json;charset=UTF-8",
		#"_security_token": "02_smlO_3naSwVeuFi"
		# "cookie":"gr_user_id=87492ae4-93ff-4347-a696-5ac8d5a7b935; security-ref=shop; _security_token_inc=91569747045399114; _security_token=02_VmIK_aLMZLzwkPq; JSESSIONID=F1E113A9AC98883E43DBF37F2DABAAA"
	}

	# print(headers)
	run=RunMethod()
	res=run.run_method('post',url,headers=header,data=None)
	print(res)
