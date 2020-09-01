import os

import yaml

class UrlUtil():

    @staticmethod
    def get_url(uri_name):
        project_path = os.path.dirname(os.getcwd())
        target_file = project_path + "/application.yml"
        with open(target_file,"r")as yaml_file:
            yaml_data = yaml.load(yaml_file,Loader=yaml.FullLoader)
            host = yaml_data["host"]
            uri = yaml_data[uri_name]
            url = host + uri
            return url

if __name__ == '__main__':
    s = UrlUtil.get_url("getdemo")
    print(s)

