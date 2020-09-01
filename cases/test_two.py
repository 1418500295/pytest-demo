import pytest,httpx,requests
from utils.http_main import HttpMain
from utils.operate_yaml import UrlUtil
from utils.operate_data import TestDataUtil
from config.logging_setting import LogConfig
from config.config_file import ConfigFile

logger = LogConfig.get_logger()


class TestTwo():

    @pytest.mark.dependency(name='getcookies')
    # @pytest.mark.run(order=1)
    def test_01(self):
        res = requests.get(UrlUtil.get_url('getcookies'))
        ConfigFile.COOKIE = res.cookies
        print("cookies是", res.cookies)
        logger.info("实际结果是"+res.text)


    @pytest.mark.dependency(depends=["getcookies"])
    @pytest.mark.skip
    # @pytest.mark.run(order=2)
    def test_02(self):
        # res = HttpMain.get_main(UrlUtil.get_url('getwithcookies'),headers={"Cookie":"login=true"})
        # print(str(res))
        res = requests.get(UrlUtil.get_url('getwithcookies'),cookies=ConfigFile.COOKIE)
        print("结果是",res.text)





#
# if __name__ == '__main__':
#     pytest.main(['-s'])