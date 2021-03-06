from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
import time
from creds import admin_login, admin_password
import random
from random import choice
from string import digits
from navigation_bar import NavigationBar
from admin_booking import AdminBookingPage
from channel_page import ChannelPage



ActivityName = "AlertTest"
ActivityTimezone = 'AT'
ChannelNameList = []
ChannelFirstLastNameList = []


class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO213_214_215_216_788(BaseTest):
    def test_213(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page = ChannelPage()
        page.open()
        page.add_channel_button.click()
        time.sleep(5)
        NewUserName = ("AutoTest_" + ''.join(choice(digits) for i in range(4)))
        page.username_field.send_keys(NewUserName)
        NewUserPassword = ('' + ''.join(choice(digits) for i in range(8)) + 'qwer')
        page.password_field.send_keys(NewUserPassword)
        NewChannelName = ("AutoTest_" + ''.join(choice(digits) for i in range(3)))
        ChannelNameList.append(NewChannelName)
        page.channel_name.send_keys(NewChannelName)
        first_names = ('Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James')
        NewFirstName = random.choice(first_names)
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff')
        NewLastName = random.choice(last_names)
        ChannelFirstLastNameList.append(NewFirstName+' '+''.join(NewLastName))
        page.last_name_field.send_keys(NewLastName)
        NewHouseNumber = '2345'
        page.house_number_field.send_keys(NewHouseNumber)
        NewStreet = 'Main Street'
        page.street_field.send_keys(NewStreet)
        select = Select(page.country_list)
        NewCountry = 'United States'
        select.select_by_visible_text(NewCountry)
        time.sleep(5)
        select = Select(page.state_list)
        NewState = 'Florida'
        select.select_by_visible_text(NewState)
        NewCity = "Miami"
        page.city_field.send_keys(NewCity)
        NewZipCode = '56788'
        page.zip_code.send_keys(NewZipCode)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.send_keys(NewPhone1)
        NewPhone2 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone2_field.send_keys(NewPhone2)
        NewEmail = ('' + ''.join(choice(digits) for i in range(10)) + '@mailinator.com')
        page.email_field.send_keys(NewEmail)
        select = Select(page.comission_type_list)
        NewComissionType = 'Percentage'
        select.select_by_visible_text(NewComissionType)
        NewComissionAmount = '15'
        page.comission_amount.send_keys(NewComissionAmount)
        NewBankName = 'BSB'
        page.bank_name_field.send_keys(NewBankName)
        select = Select(page.bank_account_type)
        NewAccountType = 'Savings'
        select.select_by_visible_text(NewAccountType)
        NewRoutingNumber = ('' + ''.join(choice(digits) for i in range(10)))
        page.routing_number_field.send_keys(NewRoutingNumber)
        NewAccountNumber = ('' + ''.join(choice(digits) for i in range(10)))
        page.account_number_field.send_keys(NewAccountNumber)
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(NewChannelName)
        time.sleep(2)
        assert page.table_channel_name.get_attribute('textContent') == NewFirstName+' '+''.join(NewLastName)+' ('+''.join(NewChannelName)+')'
        assert page.table_channel_comission.get_attribute('textContent') == NewComissionAmount+'%'
        assert page.table_channel_phonenumber.get_attribute('textContent') == NewPhone1
        assert page.table_channel_email.get_attribute('textContent') == NewEmail
        page.table_channel_editbutton.click()
        time.sleep(5)
        assert page.username_field.get_attribute('value') == NewUserName
        assert page.channel_name.get_attribute('value') == NewChannelName
        assert page.first_name_field.get_attribute('value') == NewFirstName
        assert page.last_name_field.get_attribute('value') == NewLastName
        assert page.house_number_field.get_attribute('value') == NewHouseNumber
        assert page.street_field.get_attribute('value') == NewStreet
        select = Select(page.country_list)
        assert select.first_selected_option.text == NewCountry
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewState
        assert page.city_field.get_attribute('value') == NewCity
        assert page.zip_code.get_attribute('value') == NewZipCode
        assert page.phone1_field.get_attribute('value') == NewPhone1
        assert page.phone2_field.get_attribute('value') == NewPhone2
        assert page.email_field.get_attribute('value') == NewEmail
        select = Select(page.comission_type_list)
        assert select.first_selected_option.text == NewComissionType
        assert page.bank_name_field.get_attribute('value') == NewBankName
        select = Select(page.bank_account_type)
        assert select.first_selected_option.text == NewAccountType
        assert page.routing_number_field.get_attribute('value') == NewRoutingNumber
        assert page.account_number_field.get_attribute('value') == NewAccountNumber
        assert page.status_checkbox.is_selected() == True
        page.cancel_button.click()
        time.sleep(7)
        page = NavigationBar()
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)
        page.first_tickets_type.send_keys('1')
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 30))
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(2, 10))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM', 'PM'))
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)
        time.sleep(5)
        page.enter_customer_information_button.click()
        FirstName = "Alexey"
        page.first_name.send_keys(FirstName)
        LastName = "Kolennikov"
        page.last_name.send_keys(LastName)
        EmailAddress = '6196511@mailinator.com'
        page.email_address.send_keys(EmailAddress)
        page.complete_booking_button.click()
        time.sleep(2)
        select = Select(page.channel_list)
        time.sleep(5)
        select.select_by_visible_text(NewChannelName)
        assert select.first_selected_option.text == NewChannelName

    def test_214(self):
        page = ChannelPage()
        page.open()
        time.sleep(5)
        page.search_field.send_keys(ChannelNameList[0])
        time.sleep(2)
        page.table_channel_editbutton.click()
        time.sleep(5)
        assert page.status_checkbox.is_selected() == True
        page.status_checkbox.click()
        page.save_button.click()
        time.sleep(7)
        page = NavigationBar()
        page.main_actions_drop_down.click()
        time.sleep(2)
        page.add_a_booking.click()
        page = AdminBookingPage()
        select = Select(page.activity_list)
        select.select_by_visible_text(ActivityName)
        page.first_tickets_type.send_keys('1')
        time.sleep(5)
        page.datepicker_next_month.click()
        time.sleep(5)
        EventDate = str(random.randint(2, 30))
        for i in range(0, len(page.dates)):
            if page.dates[i].get_attribute("textContent") == EventDate:
                page.dates[i].click()
            else:
                continue
            break
        time.sleep(5)
        EventTimeHours = str(random.randint(2, 10))
        minutes_values = ('00', '15', '30', '45')
        EventTimeMinutes = random.choice(minutes_values)
        timeday = random.choice(('AM', 'PM'))
        EventTimeWithZone = (EventTimeHours + ':' + ''.join(EventTimeMinutes) + ' ' + ''.join(timeday) + ' ' + ''.join(
            ActivityTimezone))
        select = Select(page.time)
        select.select_by_visible_text(EventTimeWithZone)
        time.sleep(5)
        page.enter_customer_information_button.click()
        FirstName = "Alexey"
        page.first_name.send_keys(FirstName)
        LastName = "Kolennikov"
        page.last_name.send_keys(LastName)
        EmailAddress = '6196511@mailinator.com'
        page.email_address.send_keys(EmailAddress)
        page.complete_booking_button.click()
        time.sleep(2)
        select = Select(page.channel_list)
        time.sleep(5)
        L=[]
        for i in range (0, len(page.channel_list_options)):
            L.append(page.channel_list_options[i].get_attribute("textContent"))
        assert ChannelNameList[0] not in L

    def test_215(self):
        page = ChannelPage()
        page.open()
        time.sleep(5)
        page.search_field.send_keys(ChannelNameList[0])
        time.sleep(2)
        page.table_channel_editbutton.click()
        time.sleep(5)
        NewChannelName = ("AutoTestEdited_" + ''.join(choice(digits) for i in range(3)))
        ChannelNameList.append(NewChannelName)
        page.channel_name.clear()
        page.channel_name.send_keys(NewChannelName)
        first_names = ('Ivan', 'Peter', 'John', 'Bill', 'Michael', 'Sidor', 'Alex', 'James')
        NewFirstName = random.choice(first_names)
        page.first_name_field.clear()
        page.first_name_field.send_keys(NewFirstName)
        last_names = ('Smith', 'Baker', 'Petroff', 'Smirnoff', 'Black', 'White', 'Broun', 'Ivanoff')
        NewLastName = random.choice(last_names)
        ChannelFirstLastNameList.append(NewFirstName + ' ' + ''.join(NewLastName))
        page.last_name_field.clear()
        page.last_name_field.send_keys(NewLastName)
        NewHouseNumber = '54'
        page.house_number_field.clear()
        page.house_number_field.send_keys(NewHouseNumber)
        NewStreet = '1st Avenue'
        page.street_field.clear()
        page.street_field.send_keys(NewStreet)
        select = Select(page.country_list)
        NewCountry = 'Canada'
        select.select_by_visible_text(NewCountry)
        time.sleep(5)
        select = Select(page.state_list)
        NewState = 'Alberta'
        select.select_by_visible_text(NewState)
        NewCity = "Toronto"
        page.city_field.clear()
        page.city_field.send_keys(NewCity)
        NewZipCode = 'A1A 1A1'
        page.zip_code.clear()
        page.zip_code.send_keys(NewZipCode)
        NewPhone1 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone1_field.clear()
        page.phone1_field.send_keys(NewPhone1)
        NewPhone2 = ('' + ''.join(choice(digits) for i in range(10)))
        page.phone2_field.clear()
        page.phone2_field.send_keys(NewPhone2)
        NewEmail = ('' + ''.join(choice(digits) for i in range(10)) + '@mailinator.com')
        page.email_field.clear()
        page.email_field.send_keys(NewEmail)
        select = Select(page.comission_type_list)
        NewComissionType = 'Dollar Amount'
        select.select_by_visible_text(NewComissionType)
        NewComissionAmount = '5'
        page.comission_amount.clear()
        page.comission_amount.send_keys(NewComissionAmount)
        NewBankName = 'New Bank'
        page.bank_name_field.clear()
        page.bank_name_field.send_keys(NewBankName)
        select = Select(page.bank_account_type)
        NewAccountType = 'Checking'
        select.select_by_visible_text(NewAccountType)
        NewRoutingNumber = ('' + ''.join(choice(digits) for i in range(10)))
        page.routing_number_field.clear()
        page.routing_number_field.send_keys(NewRoutingNumber)
        NewAccountNumber = ('' + ''.join(choice(digits) for i in range(10)))
        page.account_number_field.clear()
        page.account_number_field.send_keys(NewAccountNumber)
        page.save_button.click()
        assert page.status_checkbox.is_selected() == False
        page.status_checkbox.click()
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(NewChannelName)
        time.sleep(2)
        assert page.table_channel_name.get_attribute('textContent') == NewFirstName + ' ' + ''.join(
            NewLastName) + ' (' + ''.join(NewChannelName) + ')'
        assert page.table_channel_comission.get_attribute('textContent') == '$'+''.join(NewComissionAmount)
        assert page.table_channel_phonenumber.get_attribute('textContent') == NewPhone1
        assert page.table_channel_email.get_attribute('textContent') == NewEmail
        page.table_channel_editbutton.click()
        time.sleep(5)
        assert page.channel_name.get_attribute('value') == NewChannelName
        assert page.first_name_field.get_attribute('value') == NewFirstName
        assert page.last_name_field.get_attribute('value') == NewLastName
        assert page.house_number_field.get_attribute('value') == NewHouseNumber
        assert page.street_field.get_attribute('value') == NewStreet
        select = Select(page.country_list)
        assert select.first_selected_option.text == NewCountry
        select = Select(page.state_list)
        assert select.first_selected_option.text == NewState
        assert page.city_field.get_attribute('value') == NewCity
        assert page.phone1_field.get_attribute('value') == NewPhone1
        assert page.phone2_field.get_attribute('value') == NewPhone2
        assert page.email_field.get_attribute('value') == NewEmail
        select = Select(page.comission_type_list)
        assert select.first_selected_option.text == NewComissionType
        assert page.bank_name_field.get_attribute('value') == NewBankName
        select = Select(page.bank_account_type)
        assert select.first_selected_option.text == NewAccountType
        assert page.routing_number_field.get_attribute('value') == NewRoutingNumber
        assert page.account_number_field.get_attribute('value') == NewAccountNumber
        assert page.status_checkbox.is_selected() == True
        assert page.zip_code.get_attribute('value') == NewZipCode #FAILED BUG 2833
        page.cancel_button.click()

    def test_216(self):
        page = ChannelPage()
        page.open()
        time.sleep(5)
        page.search_field.send_keys(ChannelNameList[1])
        time.sleep(2)
        page.table_channel_delete_button.click()
        time.sleep(2)
        alert = get_driver().switch_to_alert()
        assert ('Are you sure you want to delete '+''.join(ChannelFirstLastNameList[1])+ ' (' + ''.join(ChannelNameList[1]) + ')?') in alert.text
        alert.accept()
        time.sleep(10)
        page.search_field.send_keys(ChannelNameList[1])
        time.sleep(2)
        assert page.table_empty.get_attribute('textContent') == 'No matching records found'

    def test_788(self):
        page = ChannelPage()
        page.open()
        page.add_channel_button.click()
        time.sleep(5)
        NewChannelName = ChannelNameList[1]
        page.channel_name.send_keys(NewChannelName)
        ChannelNameList.append(NewChannelName)
        page.save_button.click()
        time.sleep(5)
        page.search_field.send_keys(NewChannelName)
        time.sleep(2)
        assert page.table_channel_name.get_attribute('textContent') == '  ('+''.join(NewChannelName)+')'
        assert page.table_channel_comission.get_attribute('textContent') == '' #FAILED FOR PERCENTAGE - Bug 3110
        assert page.table_channel_phonenumber.get_attribute('textContent') == ''
        assert page.table_channel_email.get_attribute('textContent') == ''
        page.table_channel_editbutton.click()
        time.sleep(5)
        assert page.channel_name.get_attribute('value') == NewChannelName
        assert page.status_checkbox.is_selected() == True
        page.cancel_button.click()
