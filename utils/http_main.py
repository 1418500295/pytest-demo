import httpx
import json
from config.aes_config import AesUtil
from utils.encry_parse_data import ParseData
class HttpMain():

    @staticmethod
    def get_main(url,params=None,headers=None):

        res = None
        try:
            if headers:
                res = httpx.get(url,params=params,headers=headers)
            else:
                res = httpx.get(url,params=params)

        except RuntimeError as e:
            print("{}运行异常".format(e))

        return json.loads(AesUtil.decrypt(res.text))

    @staticmethod
    def post_main(url,data,headers=None):

        res = None
        try:
            if headers:
                res = httpx.post(url,data=data,headers=headers)
            else:
                res = httpx.post(url,data=data)

        except RuntimeError as e:
            print(e)

        return json.loads(AesUtil.decrypt(res.text))






