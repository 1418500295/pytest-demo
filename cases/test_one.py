# import pytest
# import requests
# from config.config_file import ConfigFile
# from utils.http_main import HttpMain
# from utils.operate_yaml import UrlUtil
# from utils.operate_data import TestDataUtil
# from config.logging_setting import LogConfig
# from cases.test_two import TestTwo
# logger = LogConfig.get_logger()
# class TestOne():
#
#
#     def setup(self):
#         print("单个测试开始")
#
#     def teardown(self):
#         print("单个测试结束")
#
#     # @classmethod
#     # def setup_class(cls):
#     #     # self.logger = LogConfig.get_logger()
#     #     print("当前类测试开始")
#     #
#     # @classmethod
#     # def teardown_class(cls):
#     #     print("当前类测试结束")
#     #
#     # def setup_module(self):
#     #     print("测试套件开始")
#     #
#     # def teardown_module(self):
#     #     print("测试套件结束")
#
#     def test_getdemo(self):
#         url = UrlUtil.get_url("getdemo")
#         res = HttpMain.get_main(url,params=TestDataUtil.get_test_data("getdemo.json",0))
#         print("test_getdemo:",str(res))
#
#     def test_01(self):
#         print("test_01")
#         logger.info("test01")
#
#     @pytest.mark.dependency(depends=["getcookies"])
#     # @pytest.mark.skip()
#     @pytest.mark.run(order=2)
#     def test_with_cookies(self):
#         # res = HttpMain.get_main(UrlUtil.get_url('getwithcookies'),headers={"Cookie":"login=true"})
#         # print(str(res))
#         res = requests.get(UrlUtil.get_url('getwithcookies'), cookies=ConfigFile.COOKIE)
#         print("test_with_cookies:", res.text)

# if __name__ == '__main__':
#     pytest.main(['-s'])