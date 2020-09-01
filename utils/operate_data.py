import json
import os

class TestDataUtil():

    @staticmethod
    def get_test_data(data_name,case_index):
        project_path = os.path.dirname(os.getcwd())
        target_path = project_path + "/testdata/"+ data_name
        with open(target_path,"r",encoding='utf-8') as test_file:
            test_data = json.load(test_file)
            return test_data[case_index]

if __name__ == '__main__':
    s= TestDataUtil.get_test_data("getdemo.json",0)
    print(type(s))
    print(s)