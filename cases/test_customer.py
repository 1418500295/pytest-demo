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


class TestCustomer():

    @pytest.mark.dependency(depends=['cases/test_login.py::TestLogin::test_login'],scope='package')
    @pytest.mark.run(order=2)
    def test_customer(self):
        url = UrlUtil.get_url("customer")
        headers = dict()
        headers.update(ConfigFile.set_token())
        headers.update(ParseData.parse_base())
        res = HttpMain.get_main(url, headers=headers)
        print(res)
        assert res['code'] == 200



