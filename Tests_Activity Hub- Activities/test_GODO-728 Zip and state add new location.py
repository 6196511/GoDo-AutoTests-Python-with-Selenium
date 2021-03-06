from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from starting_location import AddStartingLocationPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from creds import admin_login, admin_password
from webium import BasePage, Finds


class BaseTest(object):
    def teardown_class(self):
         close_driver()

class LocationLink(BasePage):
    location_links = Finds(by=By.XPATH, value="//a[contains(text(), 'Helena')]")



class Test_GODO728(BaseTest):
    def test_728(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.add_location_button.click()
        page = AddStartingLocationPage()
        select = Select(page.location_Country)
        select.select_by_visible_text('United States')
        select = Select(page.location_state)
        time.sleep(3)
        select.select_by_visible_text('Florida')
        page.location_zipcode.send_keys('54321')
        State = select.first_selected_option.text
        Zip = page.location_zipcode.get_attribute('value')
        select = Select(page.location_Country)
        select.select_by_visible_text('Canada')
        time.sleep(3)
        select = Select(page.location_state)
        assert select.first_selected_option.text == State
        assert page.location_zipcode.get_attribute('value') == Zip
        select = Select(page.location_Country)
        select.select_by_visible_text('Mexico')
        time.sleep(3)
        assert page.location_zipcode.get_attribute('value') == Zip
        select = Select(page.location_Country)
        select.select_by_visible_text('United States')
        time.sleep(3)
        select = Select(page.location_state)
        assert select.first_selected_option.text == State
        assert page.location_zipcode.get_attribute('value') == Zip
