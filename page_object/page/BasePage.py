# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/7/10 19:58
# 文件名：BasePage.py
# 开发工具：PyCharm
import yaml
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):  # 这里要写成构造函数
        self.driver = AndroidClient.driver

    def find(self, kv) -> WebElement:  # 如果链式调用的时候加了返回值后还没有click方法，就添加类型
        # 这里做为一个参数传进来的，所以给的参数是一个元祖(By.XPATH, "//*[@text='%s']" % text)
        return self.driver.find_element(*kv)  # 要有返回值才可以链式调用，不然就没有click方法
        # *这里是把传进来的元祖拆分成两个参数传给self.driver.find_element方法。   *这里要进步验证  如果把上面的KV改带*会是怎么样

    def findByText(self, text):
        # return self.driver.find_element(By.XPATH, "//*[@text='%s'] " % text)
        return self.find((By.XPATH, "//*[@text='%s']" % text))

    def loadstep(self, po_path, key, **kwargs):
        f = open(po_path, 'r', encoding='utf-8')  # 这里不加encoding='utf-8'会乱码
        po_data = yaml.load(f)
        # print(po_data)
        po_method = po_data[key]
        for step in po_method:
            step: dict
            element = self.driver.find_element(by=step['by'], value=step['locator'])

            if str(step['action']).lower() == 'click':
                element.click()
            elif str(step['action']).lower() == 'sendkeys':  # 这里的'sendkeys'要和.yaml中的sendkeys一致
                text = str(step['text'])
                print('\n .yaml: '+text)
                for k, v in kwargs.items():  # 这里是取传进来的变量
                    print('打印传进来的参数k：' + k, '打印传进来的参数v：'+ v)
                    # text2 = text.replace(step['text'], v)    # 我写的，不对
                    print('旧字符串'+("$%s" % k))
                    print('替换前的text :' + text)
                    text = text.replace("$%s" % k, v)              # "$%s" % k  理解成.yaml中要替换的变量     旧字符串和替换前的text 的一致才会替换
                    print("update text: %s" % text)
                print("变量 : %s" % text)
                element.send_keys(text)
            else:
                print("UNKNOW COMMAND  %s" % step)
