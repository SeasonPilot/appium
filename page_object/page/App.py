# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/7/10 19:07
# 文件名：App.py
# 开发工具：PyCharm
from page_object.driver.AndroidClient import AndroidClient
from page_object.page.MainPage import MainPage


class App:
    @classmethod             # 这里要写类方法，可以省的初始化
    def main(cls):           # 这里要改成cls，不应该是self
        AndroidClient.restart_app()
        return MainPage()