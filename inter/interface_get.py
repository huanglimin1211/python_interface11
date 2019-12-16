#coding=utf-8
import requests
import json,time
class Run_Main():
    def __init__(self,url,data,method):
        self.res=self.run_main(url,data,method)
              
    def request_post(self,url,data):    
        res=requests.post(url=url,data=data).json()
        # res=json.dumps(res,sort_keys=True,indent=4)//
        # print(res)
        return res

    def request_get(self,url,data=None):
        res=requests.get(url=url,data=None).json()
        return res

    def run_main(self,url,data,method):
        if method=='POST':
            return self.request_post(url,data)
        if method=='GET':
            return self.request_get(url,data)

class Request_Get():
    """docstring for request_get"""
    def __init__(self, url,headers):
        self.url=url
        self.headers=headers
        
    def interface_login(self):
        self.res=requests.get(self.url,self.headers)
        self.text=self.res.text
        print(self.text)
        print(str(self.res.status_code)+'*************************')#print要放在return之前
        return self.res


class Request_Post():
    """docstring for request_get"""

    def __init__(self, url, headers,data):
        self.data=data
        self.url = url
        self.headers = headers


    def interface_post(self):
        self.res = requests.post(self.url, self.headers,self.data)
        self.text = self.res.text
        print(self.text)
        print(str(self.res.status_code) + '*************************')  # print要放在return之前
        return self.res
if __name__ == '__main__':
    url = 'http://detection.dev.dasouche.net/jiaxuanreport/jxDetectAction/selectCheckResultMsg.json?'
    data= '{"carId": "35bff94b6b394e5eafb2280b2784fd15"}'
    header = {
        'Content-Type':'application/x-www-form-urlencoded',
        # "Souche-Security-Token": "02_2LDV_3naSwVeuFi",
        "_security_token": "02_i4FT_3naSwVeuFi"
        # "cookie":"gr_user_id=87492ae4-93ff-4347-a696-5ac8d5a7b935; security-ref=shop; _security_token_inc=91569747045399114; _security_token=02_VmIK_aLMZLzwkPq; JSESSIONID=F1E113A9AC98883E43DBF37F2DABAAA"
    }
    print(type(data))
    req=Request_Post(url=url,headers=header,data=data)
    req.interface_post()


    # url='https://www.apiopen.top/weatherApi'
    # data={'city':"北京"}
    # req=Run_Main(url,data,'POST')
    # res=req.run_main(url,data,'POST')
    # print(res)
    # print(res['data'])
    # print(type(res))
    # if res['code']==200:
    #     print("测试用例通过")
    # else:
    #     print("测试用例失败")


