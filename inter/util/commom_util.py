# coding= utf-8
import json


class Common_Util(object):
    """docstring for Common_Util"""

    def is_contain(self, str_one, str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag


if __name__ == '__main__':
    common = Common_Util()
    expect = "'该车外观: 12345678901234567890认证描述这里有30字；内饰: 12345678901234567890认证描述这里有30字；其他: 12345678901234567890认证描述这里有30字'"
    res = {
        "code": "200",
        "data": "该车外观: 12345678901234567890认证描述这里有30字；内饰: 12345678901234567890认证描述这里有30字；其他: 12345678901234567890认证描述这里有30字",
        "msg": "success",
        "success": "true",
        "traceId": "z73air"
    }
    res = json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)
    flag=common.is_contain(expect, res)
    print(flag)
