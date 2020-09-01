import httpx
import json
class HttpMain():

    @staticmethod
    def get_main(url,params=None,headers=None):
        res = None
        try:
            if headers:
                res = httpx.get(url,params=params,headers=headers).json()
            else:
                res = httpx.get(url,params=params).json()
        except RuntimeError as e:
            print("{}运行异常".format(e))

        return res

    @staticmethod
    def post_main(url,data,headers=None):
        res = None
        try:
            if headers:
                res = httpx.post(url,data=data,headers=headers).json()
            else:
                res = httpx.post(url,data=data).json()
        except RuntimeError as e:
            print(e)

        return res






