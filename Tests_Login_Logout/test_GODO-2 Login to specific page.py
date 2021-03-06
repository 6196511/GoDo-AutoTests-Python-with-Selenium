from selenium.webdriver.common.by import By
from webium import BasePage, Find
from webium.driver import get_driver
from webium.driver import close_driver
from creds import admin_login, admin_password



class BaseTest(object):
    def teardown_class(self):
         close_driver()

class loginpage (BasePage):
    url = 'https://dev.godo.io/customer_list.aspx'
    login_field = Find(by=By.NAME, value='username')
    password_field = Find(by=By.NAME, value='password')
    button = Find(by=By.XPATH, value='//input[@class="btn-sm btn-primary"]')

class Test_GODO2(BaseTest):
    def test_2(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        assert get_driver().current_url == 'https://dev.godo.io/customer_list.aspx'
        get_driver().quit()
