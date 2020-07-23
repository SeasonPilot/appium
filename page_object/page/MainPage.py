from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage
from selenium.webdriver.common.by import By
import yaml


class MainPage(BasePage):  # 继承BasePage
    _profile_button = (By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")

    def gotoSelected(self):
        # 调用全局的driver对象使用webdriver api操纵app
        # self.driver.find_element_by_xpath("//*[@text='自选']")
        # 第一次改造
        # self.driver.find_element(By.XPATH, "//*[@text='自选']")
        # 第二次改造
        # BasePage().find(By.XPATH, "//*[@text='自选']")   # 要写成self.find
        # self.find(By.XPATH, "//*[@text='自选']")
        # 第三次改造
        # zixuan = (By.XPATH, "//*[@text='自选']")
        # self.find(zixuan)
        # 第四次改造
        zixuan = '自选'

        # self.driver.find_element_by_xpath("//*[@text='自选']").click()
        # self.driver.find_element(By.XPATH, "//*[@text='自选']").click()
        self.findByText(zixuan)
        self.findByText(zixuan).click()
        return SelectedPage()

    def gotoSearch(self) -> SearchPage:
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        # self.find(MainPage._profile_button).click()  # 访问类变量要加类名
        self.loadstep('../data/MainPage.yaml', 'gotoProfile')
        return ProfilePage()
