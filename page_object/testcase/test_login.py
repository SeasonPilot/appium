import pytest

from page_object.page.App import App


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().gotoProfile()

    def setup_method(self):
        self.loginPage = self.profilePage.gotoLogin()

    @pytest.mark.parametrize("user, pw, msg", [
        ("156005347600", "111111", "手机号码"),
        ("15600534760", "111111", "密码错误")
    ])
    def test_login_password(self, user, pw, msg):  # 忘记写形参了
        self.loginPage.loginByPassword(user, pw)        # user 是变量  不能加双引号
        assert msg in self.loginPage.getErrorMsg()      # msg 是变量  不能加双引号

    def teardown_method(self):
        self.loginPage.back()
