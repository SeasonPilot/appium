# _*_ coding:utf-8 _*_
# 作者：Administrator
# 时间：2020/7/12 13:32
# 文件名：SearchPage.py
# 开发工具：PyCharm
from time import sleep

from selenium.webdriver.common.by import By
from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    def search(self, key):
        # 搜索框定位符
        edit_locator = (By.CLASS_NAME, "android.widget.EditText")
        self.find(edit_locator).send_keys(key)
        return self  # 还在当前页面   为了可以链式调用

    def addToSelected(self, key):
        # name = ("//*[contains(@resource-id, 'stockCode') and contains(@text=%s)]" % key +          # %s有单引号，忘记写By.XPATH了
        #         "/../../..//*[contains(@resource-id, 'follow')]")
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and @text='%s']" % key +
                         "/../../..//*[contains(@resource-id, 'follow_btn')]")

        self.find(follow_button).click()
        return self  # 还在当前页面   为了链式调用

    def removeFromSelected(self, key):
        followed_button = (By.XPATH,
                           "//*[contains(@resource-id, 'stockCode') and @text='%s']" % key +
                           "/../../..//*[contains(@resource-id, 'followed_btn')]")

        self.find(followed_button).click()
        return self  # 还在当前页面   为了链式调用

    def isInSelected(self, key):
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text, '%s')]" % key +
                         "/../../..//*[contains(@resource-id, 'follow')]")  # %s有单引号，忘记写By.XPATH了
        #  不论是follow还是followed都可以找到

        id = self.find(follow_button).get_attribute('resourceId')  # 不是.text而是get_attribute()
        # 属性的resourceId是这样写的

        print(id)
        return 'followed_btn' in id

    def cancle(self):
        self.findByText("取消").click()

    def searchByUser(self, key):
        # todo:作业2
        # edit_locator = (By.CLASS_NAME, 'android.widget.EditText')
        user_button = (
        By.XPATH, '//*[contains(@resource-id, "ti_tab_indicator")]//*[contains(@text, "用户")]')  # 父子关系要分开写，同级别关系用and连接
        # self.find(edit_locator).send_keys(key)
        self.search(key)
        self.find(user_button).click()
        return self

    def isFollowed(self, key):
        # todo:作业2
        followed_button = (By.XPATH,
                           '//*[contains(@resource-id, "lv_list_view")]//*[@text="%s"]' % key + '/../..//*[contains(@text, "关注")]')
        id = self.find(followed_button).get_attribute("text")
        print(id)
        return '已关注' in id  # return一个结果，不要在这里断言，去用例里面进行断言
