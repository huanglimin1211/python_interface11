#coding=utf-8
class Glob_Var():

    Id="0"
    model="1"
    url="2"
    is_run="3"
    Type="4"
    cookie="5"
    case_depend="case依赖"
    field_depend="依赖的返回"
    data_depend="数据依赖字"
    data="6"
    exp_result="7"
    real_result="8"

def get_id():
	return Glob_Var.Id
def get_model():
	return Glob_Var.model
def get_url():
	return Glob_Var.url
def get_run():
	return Glob_Var.is_run

def get_type():
	return Glob_Var.Type
def get_header():
	return Glob_Var.cookie
def get_header_value():
	header={
	"security_token": "02_4jAd_GL6biuFL6C"
	}
def get_data():
	return Glob_Var.data
def get_expect():
	return Glob_Var.exp_result
def get_result():
	return Glob_Var.real_result


if __name__ == '__main__':
	res=get_type()
	print(res)
