from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from Logout import logoutpage
from selenium.webdriver.support.wait import WebDriverWait
from creds import admin_login, admin_password


class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test_GODO3(BaseTest):
    def test_3(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = logoutpage()
        page.profile_dropdown.click()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('logout_button'))
        page.logout_button.click()
        assert get_driver().current_url == 'https://dev.godo.io/login.aspx'
        get_driver().quit()