import os

import pytest
project_path = os.path.dirname(os.getcwd())
target_path = project_path + "/cases/"

if __name__ == '__main__':
    pytest.main(['-s',target_path,"--pytest_report", "../report/report.html"])
