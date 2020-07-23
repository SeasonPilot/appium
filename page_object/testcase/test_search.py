import pytest

from page_object.page.App import App
from page_object.page.MainPage import MainPage
from page_object.page.SearchPage import SearchPage


class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage = App.main()

    def setup_method(self):
        # todo:  这里访问不到类变量
        self.mainPage: MainPage = TestSelected.mainPage
        self.searchPage = self.mainPage.gotoSearch()

    def teardown_method(self):
        self.searchPage.cancle()

    def test_is_selected_stock(self):
        # searchPage = self.mainPage.gotoSearch().search('alibaba')
        # 改造
        self.searchPage.search('alibaba')
        # SearchPage.addToSelected()        #这样写不对，没有完整的流程
        assert self.searchPage.isInSelected('BABA') == True
        assert self.searchPage.isInSelected('9988') == False

    def test_is_follow_user(self):
        # todo:作业2
        key = "seven"
        self.search_user = self.searchPage.searchByUser(key)
        assert self.search_user.isFollowed(key) == False

    @pytest.mark.parametrize("key, code", [
        ("招商银行", "SH600036"),
        ("平安银行", "SZ000001"),
        ("pingan", "SH601318")
    ])     # 只作用于这一个方法
    def test_is_selected_stock_hs(self, key, code):
        # assert SearchPage.isInSelected("招商银行")==False  错误的，没有完整的流程
        self.searchPage.search(key)
        assert self.searchPage.isInSelected(code) == False

    def test_add_stock_hs(self):
        key = "招商银行"
        code = "SH600036"
        self.searchPage.search(key)
        if self.searchPage.isInSelected(code):
            self.searchPage.removeFromSelected(code)
        self.searchPage.addToSelected(code)
        assert self.searchPage.isInSelected(code) == True
