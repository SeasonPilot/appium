from selenium.webdriver.common.by import By

from page_object.driver.AndroidClient import AndroidClient
from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):  # 继承BasePage
    def addDefault(self):
        return self

    def getPriceByName(self, name):
        # todo:
        # price = self.driver \
        #     .find_element_by_xpath("//*[contains(@resource-id, 'stockName') and @text='" + name + "']" +
        #                            "/../../..//*[contains(@resource-id, 'currentPrice')]").text
        priceLocator = By.XPATH, "//*[contains(@resource-id, 'stockName') and @text='%s']" % name +\
                     "/../../..//*[contains(@resource-id, 'currentPrice')]"
        price = self.find(priceLocator).text

        return float(price)
