from utils.operate_data import TestDataUtil
from config.aes_config import AesUtil
import json
class ParseData():

    @staticmethod
    def parse_base():
        base = TestDataUtil.get_test_data("base.json",0)
        parse_base = AesUtil.encrypt1(json.dumps(base))
        base = dict()
        base['base'] = parse_base
        return base


    @staticmethod
    def parse_data(file_name,case_index):
        data = TestDataUtil.get_test_data(file_name,case_index)
        parse_data = AesUtil.encrypt1(json.dumps(data))
        data = dict()
        data['data'] = parse_data
        return data

if __name__ == '__main__':
    print(ParseData.parse_base())


