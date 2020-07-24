import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    driver: WebDriver
    platform='android'
    @classmethod
    def install_app(cls) -> WebDriver:
        # caps = {}
        # # 如果有必要，进行第一次安装
        # # caps["app"]=''
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # # 解决第一次启动的问题
        # caps["autoGrantPermissions"] = "true"
        # # caps['noReset']=True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(10)
        # return cls.driver
        return cls.init_driver('install_app')

    @classmethod
    def restart_app(cls) -> WebDriver:
        # caps = {}
        #
        # caps["platformName"] = "android"
        # caps["deviceName"] = "hogwarts"
        # caps["appPackage"] = "com.xueqiu.android"
        # caps["appActivity"] = ".view.WelcomeActivityAlias"
        # # 为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        # caps['noReset'] = True
        # caps['chromedriverExecutableDir'] = "/Users/seveniruby/projects/chromedriver/2.20"
        # # caps["udid"]="emulator-5554"
        #
        # cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver.implicitly_wait(10)
        # return cls.driver
        return cls.init_driver('restart_app')

    @classmethod
    def init_driver(cls, key):
        with open('../data/driver.yaml', 'r') as f:
            driver_data = yaml.load(f)
        platform = driver_data['platform']
        cls.platform=platform  # 把从.yaml中读取到的被测平台名称赋值给类变量
        server = driver_data[key]['server']
        caps = driver_data[key]['caps'][platform]
        implicitly_wait = driver_data[key]['implicitly_wait']

        cls.driver = webdriver.Remote(server, caps)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver
