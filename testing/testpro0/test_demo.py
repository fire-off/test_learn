# import pytest
# import yaml
#
#
# class TestDemo:
#     @pytest.mark.parametrize("env",yaml.safe_load(open("\pycharm\project/testpro0\env.yaml")))
#     def test_demo(self,env):
#         if "test" in env:
#             print("ceshi ")
#             print("测试环境的ip是：",env["test"])
#         elif "def" in env:
#             print("kaifa")
from selenium import webdriver
driver = webdriver.Chrome()
url = 'https ://www.csdn .net/'
driver.get(url)
driver.maximize_window()

