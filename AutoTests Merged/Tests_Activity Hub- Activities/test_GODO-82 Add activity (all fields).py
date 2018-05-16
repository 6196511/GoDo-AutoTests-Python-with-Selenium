from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice
from string import digits
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

class BaseTest(object):
    def teardown_class(self):
         close_driver()

class Test1(BaseTest):
    def test_82(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys('devtester')
        page.password_field.send_keys('nf')
        page.button.click()
        page=ActivityHubPage()
        page.open()
        page.add_activity_button.click()
        page=AddEditActivityPage()
        time.sleep(15)
        NewActivityName = ("AutoTest"+''.join(choice(digits) for i in range(4)))
        page.activity_name.send_keys(NewActivityName)
        NewActivityURL = ("http://"+NewActivityName+'.com')
        page.activity_url.send_keys(NewActivityURL)
        # page.activity_status.click()
        # WebDriverWait(get_driver(), 5)
        # wait = WebDriverWait(get_driver(), 15)
        # element = wait.until(EC.text_to_be_present_in_element((By.ID, "activity_status"), "Choose Activity Status"))
        select = Select(page.activity_status)
        select.select_by_visible_text("Active")
        # page.branch.click()
        select = Select(page.branch)
        select.select_by_visible_text("First branch")
        # page.starting_location.click()
        select = Select(page.starting_location)
        select.select_by_visible_text("Hotel California")
        # page.time_zone.click()
        select = Select(page.time_zone)
        select.select_by_visible_text("Central")
        page.activity_description.send_keys('The activity is created automatically.')
        page.cancellation_policy.send_keys('We can cancel an event any time we want.')
        page.sales_tax.send_keys('5')
        page.activity_duration_days.send_keys('0')
        page.activity_duration_hours.send_keys('2')
        page.activity_duration_minutes.send_keys('15')
        select = Select(page.activity_color)
        select.select_by_visible_text("Alabaster")
        page.ticket_maximum.clear()
        page.ticket_maximum.send_keys('100')
        page.sell_out_alert.click()
        select = Select(page.sell_out_alert)
        select.select_by_visible_text("80%")
        page.alert_guide_upon_sellout.click()
        select = Select(page.alert_guide_upon_sellout)
        select.select_by_visible_text("No")
        page.stop_booking_sold.click()
        select = Select(page.stop_booking_sold)
        select.select_by_visible_text("1h 30 m")
        page.ticket_minimum.send_keys('20')
        page.minimum_not_met_alert.send_keys('10')
        page.stop_no_sales.send_keys('10')
        # page.stop_midnight_before.click()
        # page.first_sale_closes_event.click()
        # page.add_ticket_type.click()
        page.first_ticket_type.send_keys('Adult')
        page.first_ticket_price.send_keys('9.99')
        # page.first_guide.click()
        select = Select(page.first_guide)
        select.select_by_visible_text("Holly Flat")
        # page.first_linked_activity.click()
        select = Select(page.first_linked_activity)
        select.select_by_visible_text("AlertTest1")
        page.what_included.send_keys('Good mood.')
        page.what_know.send_keys('Everything will be fine.')
        page.what_bring.send_keys('Just bring a lot of money.')
        # page.review_redirect.click()
        select = Select(page.review_redirect)
        select.select_by_visible_text("5 Stars")
        page.review_website.send_keys(NewActivityURL)
        page.save_button.click()
        page = ActivityHubPage()
        page.search_activity_field.send_keys(NewActivityName)
        page.activity_actions.click()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('activity_actions'))
        text = page.activity_title.get_attribute("textContent")
        assert text == NewActivityName
        # assert page.is_element_present('activity_actions')
        # page.activity_actions.click()
        # wait = WebDriverWait(get_driver(), 15)
        # wait.until(lambda driver: page.is_element_present('edit_activity'))
        # page.edit_activity.click()