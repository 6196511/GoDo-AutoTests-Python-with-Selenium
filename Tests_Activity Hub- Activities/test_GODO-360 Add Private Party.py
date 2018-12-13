from webium.driver import get_driver
from webium.driver import close_driver
from Login import loginpage
from selenium.webdriver.support.ui import Select
from activity_hub_page import ActivityHubPage
from activity_page import AddEditActivityPage, switcher_OFF
import time
from event_schelduler import EventScheldulerPage
from creds import admin_login, admin_password,server, database, username, password
import random
from random import choice
from string import digits
import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.wait import WebDriverWait
import pyodbc

ActivityNameList =[]

class BaseTest(object):
    def teardown_class(self):
        close_driver()

class Test_GODO360(BaseTest):

    def test_360(self):
        get_driver().maximize_window()
        page = loginpage()
        page.open()
        page.login_field.send_keys(admin_login)
        page.password_field.send_keys(admin_password)
        page.button.click()
        page=ActivityHubPage()#STEP1
        page.open()
        page.add_activity_button.click()
        page=AddEditActivityPage()#STEP2
        time.sleep(15)
        NewActivityName = ("PrivatePartyAutoTest360_"+''.join(choice(digits) for i in range(4)))
        ActivityNameList.append(NewActivityName)
        page.activity_name.send_keys(NewActivityName)
        select = Select(page.activity_status)
        NewActivityStatus = "Private Party"
        select.select_by_visible_text(NewActivityStatus)
        select = Select(page.branch)
        NewActivityBranch = "AlexeyBranch"
        select.select_by_visible_text(NewActivityBranch)
        select = Select(page.starting_location)
        NewActivityLocation = "Hotel California"
        select.select_by_visible_text(NewActivityLocation)
        select = Select(page.time_zone)
        NewActivityTimezone = "Pacific"
        select.select_by_visible_text(NewActivityTimezone)
        NewActivityCancellationPolicy = 'We can cancel an event any time we want.'
        page.cancellation_policy.send_keys(NewActivityCancellationPolicy)
        NewActivityDurationMinutes = '15'
        page.activity_duration_minutes.send_keys(NewActivityDurationMinutes)
        page.ticket_maximum.clear()
        NewActivityMaxTickets = '100'
        page.ticket_maximum.send_keys(NewActivityMaxTickets)
        NewActivityFirstTicketType = "Adult"
        page.first_ticket_type.send_keys(NewActivityFirstTicketType)
        NewActivityFirstTicketPrice = '9.99'
        page.first_ticket_price.send_keys(NewActivityFirstTicketPrice)
        page.stop_booking_sold.click()
        select = Select(page.stop_booking_sold)
        NewActivityStopbookingSold = "15 m"
        select.select_by_visible_text(NewActivityStopbookingSold)
        NewActivityMinTickets = '2' #MIN TICKETS #STEP3
        page.ticket_minimum.send_keys(NewActivityMinTickets)
        assert page.switchers1[0].get_attribute("outerHTML") == switcher_OFF#Stop Booking Midnight Before
        assert page.switchers2[0].get_attribute("outerHTML")== switcher_OFF#First Sale Closes Event
        assert page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF#Tickets Minimum Enforce
        page.save_button.click() #STEP5
        time.sleep(5)
        page = ActivityHubPage()
        page.search_activity_field.send_keys(NewActivityName)
        time.sleep(5)
        page.activity_actions.click()#STEP6
        text = page.activity_title.get_attribute("textContent")
        assert text == NewActivityName
        page.edit_activity.click()#STEP7
        page = AddEditActivityPage()
        time.sleep(15)
        assert page.activity_name.get_attribute('value') == NewActivityName
        select = Select(page.activity_status)
        assert select.first_selected_option.text == NewActivityStatus
        select = Select(page.branch)
        assert select.first_selected_option.text == NewActivityBranch
        select = Select(page.starting_location)
        assert select.first_selected_option.text == NewActivityLocation
        select = Select(page.time_zone)
        assert select.first_selected_option.text == NewActivityTimezone
        assert page.cancellation_policy.get_attribute('value') == NewActivityCancellationPolicy
        assert page.activity_duration_minutes.get_attribute('value') == NewActivityDurationMinutes
        assert page.ticket_maximum.get_attribute('value') == NewActivityMaxTickets
        assert page.first_ticket_type.get_attribute('value') == NewActivityFirstTicketType
        assert page.first_ticket_price.get_attribute('value') == NewActivityFirstTicketPrice
        assert page.ticket_minimum.get_attribute('value') == NewActivityMinTickets
        for i in range(0, len(page.switchers1)):
            assert page.switchers1[i].get_attribute("outerHTML") == switcher_OFF
        for i in range(0, len(page.switchers2)):
            assert page.switchers2[i].get_attribute("outerHTML") == switcher_OFF
        assert page.switcher_minimum_enforce.get_attribute("outerHTML") == switcher_OFF
        select = Select(page.stop_booking_sold)
        assert select.first_selected_option.text == NewActivityStopbookingSold
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)#STEP8
        cursor = cnxn.cursor()
        cursor.execute("SELECT TOP 1 * FROM activity ORDER BY activity_id DESC")
        row = cursor.fetchone()
        assert row[1] == 68#company id
        assert row[2] == 47#location_id
        assert row[3] == 386#branch_id
        assert row[4] == 9 #timezone_id
        assert row[6] == NewActivityName
        assert row[11] == NewActivityCancellationPolicy
        assert row[14] == 0#Firstsalecloseevent
        assert row[15] == 0  # StopBookingNoSales
        assert row[16] == 15  # StopBookingSold
        assert row[17] == 0  # StopBookingMidBefore
        assert row[21] == 15 #Duration
        assert row[32] == True #GuideUponSellout
        assert row[33]==2 #ActivityStatus
        assert row[36] == 0 #Tickets Minimum Enforce
        assert row[37] == 0  # Viator
        assert row[39] == 0  # 2-step Check In
        page.cancel_button.click()#STEP9
        page = ActivityHubPage()
        time.sleep(5)
        page.search_activity_field.send_keys(NewActivityName)#STEP10
        time.sleep(5)
        page.activity_actions.click()#STEP11
        page.add_events.click()#STEP12
        page = EventScheldulerPage()
        wait = WebDriverWait(get_driver(), 15)
        wait.until(lambda driver: page.is_element_present('scheldule_type'))
        select = Select(page.scheldule_type)
        select.select_by_visible_text('Repeating Event (Once Per Day)')#STEP13
        page.rep_begin_field.click()#STEP14
        page.next_button_calendar_begin.click()
        NewDateBegin = random.randint(8, 20)
        nextMonthDate = datetime.date.today() + relativedelta(months=1)
        for i in range(0, len(page.date_calendar)):
            if i + 1 == NewDateBegin:
                page.date_calendar[i].click()
            else:
                continue
            break
        time.sleep(5)
        NewDateEnd = NewDateBegin + 7
        page.rep_end_field.click()
        page.next_button_calendar_enddate_rep.click()
        time.sleep(5)
        end_date_list = []
        for i in range(0, len(page.date_calendar_end)):
            if page.date_calendar_end[i].is_displayed():
                end_date_list.append(page.date_calendar_end[i])
        for i in range(0, len(end_date_list)):
            if i + 1 == NewDateEnd:
                end_date_list[i].click()
            else:
                continue
            break
        NewTimeHours = str(random.randint(1, 12))
        select = Select(page.rep_hour)
        select.select_by_visible_text(NewTimeHours)
        minutes_values = ('00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55')
        NewTimeMinutes = random.choice(minutes_values)
        select = Select(page.rep_minute)
        select.select_by_visible_text(NewTimeMinutes)
        NewTimeAMPM = random.choice(('AM','PM'))
        select = Select(page.rep_ampm)
        select.select_by_visible_text(NewTimeAMPM)
        page.rep_add.click() #STEP15
        time.sleep(5)
        assert page.is_element_present('popup_OK') == True
        page.popup_OK.click()#STEP16
        time.sleep(5)
        page=ActivityHubPage()
        assert get_driver().current_url==page.url