import time,os,sys
import unittest
import HTMLTestRunner
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from interface_get  import Run_Main
from util.operate_excel import OperateExcel
from util.smtp_email import  Send_Email
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication



class Test(unittest.TestCase):
    '''查询天气'''
    def setUp(self):
        pass
        print("qian#######################")
    def  tearDown(self):
        pass
    def testweather_01(self):
        '''查询天气API接口'''
        url='https://www.apiopen.top/weatherApi'
        data=None
        self.req=Run_Main(url,data,'POST')
        self.res=self.req.run_main(url,data,'POST')
        self.assertEqual(self.res['code'],200)
          

    def testbeijing_02(self):
        '''查询北京天气接口'''
        self.filepath=os.path.abspath("./data_config/Interface.xlsx")
        self.operate=OperateExcel(self.filepath,0)
        url=self.operate.get_cell(2,1)
        data=self.operate.get_cell(2,3)
        print(url)
        print(data)
        # url='https://www.apiopen.top/weatherApi'
        # data={'city':"北京"}
        self.req=Run_Main(url,data,'POST')
        self.res=self.req.run_main(url,data,'POST')
        print(self.res['data']['city'])
        self.assertEqual(self.res['code'],200,'The result is False')
        self.assertEqual(self.res['data']['city'],'北京')
        self.assertEqual(self.res['msg'],'成功!')




if __name__ == '__main__':
    # unittest.main()
    # 测试报告----测试用例集和测试报告
    suite=unittest.TestSuite()
    suite.addTest(Test('testweather_01'))
    suite.addTest(Test('testbeijing_02'))
    tim0=time.strftime('%Y-%m-%d')
    fp=open(os.path.abspath('./report/'+tim0+'Test.html'),'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"接口自动化测试报告")
    runner.run(suite)
    fp.close()
    mail_url=os.path.abspath('./report/'+tim0+'Test.html')
    content = "hello,my name is lmhuang"
    #调用其他模块----邮件发送的接口
    mail=Send_Email(mail_url,content)
    mail.send_email()


