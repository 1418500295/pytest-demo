import pytest,httpx,requests
from utils.http_main import HttpMain
from utils.operate_yaml import UrlUtil
from utils.operate_data import TestDataUtil
from config.logging_setting import LogConfig
from config.config_file import ConfigFile

logger = LogConfig.get_logger()


class TestTwo():



    @pytest.mark.dependency(name='getcookies')
    @pytest.mark.run(order=1)
    # @pytest.fixture(autouse=True)
    def test_get_cookies(self):
        res = requests.get(UrlUtil.get_url('getcookies'))
        ConfigFile.COOKIE = res.cookies
        print("cookies是:", res.cookies)
        # logger.info("实际结果是"+res.text)




    # @pytest.fixture(scope='class',autouse=True)
    # def test_03(self):
    #     print("开始")
    #     yield
    #     print("结束")
    #     print("test_03")






if __name__ == '__main__':
    pytest.main(['-s','test_two.py'])