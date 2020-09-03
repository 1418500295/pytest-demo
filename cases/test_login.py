import pytest
import requests
from config.config_file import ConfigFile
from utils.http_main import HttpMain
from utils.operate_yaml import UrlUtil
from utils.operate_data import TestDataUtil
from config.logging_setting import LogConfig
from utils.encry_parse_data import ParseData
from config.aes_config import AesUtil
import json
logger = LogConfig.get_logger()


class TestLogin():

    @pytest.mark.dependency()
    @pytest.mark.run(order=1)
    def test_login(self):
        url = UrlUtil.get_url("login")
        data = ParseData.parse_data("login.json",0)
        res = HttpMain.post_main(url,data=data,headers=ParseData.parse_base())
        ConfigFile.TOKEN = res['data']['access_token']
        print(ConfigFile.TOKEN)
        assert res['code'] == 200

    @pytest.mark.dependency(depends=["TestLogin::test_login"])
    @pytest.mark.run(order=2)
    def test_room_info(self):
        url = UrlUtil.get_url("room_info")
        headers = dict()
        headers.update(ConfigFile.set_token())
        headers.update(ParseData.parse_base())
        res = HttpMain.get_main(url,headers=headers)
        assert res['code'] == 200



# if __name__ == '__main__':
#     pytest.main(['-s'])


