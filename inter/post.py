#coding=utf-8
import requests,json

url = 'http://detection.dev.dasouche.net/jiaxuanreport/jxDetectAction/saveJxReportInfo.json?'
fp= open('./data_config/save_renzheng.json')
# data1=json.load(fp)
# data = json.dumps(data1)
# print(type(data))
data=fp.read()
data1=json.loads(data)
data=json.dumps(data1)
headers = {
	"Content-Type": "application/json;charset=UTF-8",
	"_security_token": "02_04cs_3naSwVeuFi"
	# "cookie":"gr_user_id=87492ae4-93ff-4347-a696-5ac8d5a7b935; security-ref=shop; _security_token_inc=91569747045399114; _security_token=02_VmIK_aLMZLzwkPq; JSESSIONID=F1E113A9AC98883E43DBF37F2DABAAA"
}
res=requests.post(url,data=data,headers=headers).json()
print(res)