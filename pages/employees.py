from selenium.webdriver.common.by import By
from webium import BasePage, Find, Finds


class EmployeePage(BasePage):
    url = 'https://ci004.godo.io/administrator.aspx'
    user_entry = Finds(by=By.XPATH, value="//tr[@class='ng-scope odd']|//tr[@class='ng-scope even']")
    edit_user_button = Find(by=By.XPATH, value="//i[@class='fa fa-edit']")
    delete_user_button = Find(by=By.XPATH, value="//i[@class='fa fa-remove']")
    search_field = Find(by=By.XPATH, value="//input[@type='search']")
    add_new_user = Find(by=By.XPATH, value="//button[@id='addUser']")
    username_field = Find(by=By.XPATH, value="//input[@name='administrator_username']")
    password_field = Find(by=By.XPATH, value="//input[@name='administrator_password']")
    first_name_field = Find(by=By.XPATH, value="//input[@id='administrator_firstname']")
    last_name_field = Find(by=By.XPATH, value="//input[@id='administrator_lastname']")
    phone1_field = Find(by=By.XPATH, value="//input[@id='administrator_phone_1']")
    phone2_field = Find(by=By.XPATH, value="//input[@id='administrator_phone_2']")
    email_field = Find(by=By.XPATH, value="//input[@id='administrator_email']")
    role_list = Find(by=By.XPATH, value="//select[@id='administrator_role']")
    payroll_type_list = Find(by=By.XPATH, value="//select[@id='administrator_payment_type']")
    amount_field = Find(by=By.XPATH, value="//input[@id='administrator_payment_amount']")
    status_checkbox = Find(by=By.XPATH, value="//input[@id='administrator_status']")
    hire_date_field = Find(by=By.XPATH, value="//input[@id='administrator_startdate']")
    end_date_field = Find(by=By.XPATH, value="//input[@id='administrator_enddate']")
    calendar_begin_next = Finds(by=By.XPATH, value="//th[@class='next']")
    calendar_begin_prev = Finds(by=By.XPATH, value="//th[@class='prev']")
    dates_calendar_begin = Finds(by=By.XPATH, value="//td[@class='day']")
    calendar_end_next = Finds(by=By.XPATH, value="//th[@class='next']")
    calendar_end_prev = Finds(by=By.XPATH, value="//th[@class='prev']")
    dates_calendar_end = Finds(by=By.XPATH, value="//td[@class='day']")
    save_button = Find(by=By.XPATH, value="//button[@id='submituser']")
    country_list = Find(by=By.XPATH, value="//select[@id='administrator_country']")
    state_list = Find(by=By.XPATH, value="//select[@id='administrator_state']")
    user_zip = Find(by=By.XPATH, value="//input[@id='administrator_zipCode']")
    branch_list = Find(by=By.XPATH, value="//select[@id='branch_id']")
    name_account_owner_field = Find(by=By.XPATH, value="//input[@id='administrator_bank_nameonaccount']")
    bank_name_field = Find(by=By.XPATH, value="//input[@id='administrator_bank_name']")
    routing_number_field = Find(by=By.XPATH, value="//input[@id='administrator_bank_routingnumber']")
    account_number_field = Find(by=By.XPATH, value="//input[@id='administrator_bank_accountnumber']")
    username_readonly_field = Find(by=By.XPATH, value="//input[@ng-value='vm.user.username']")
    house_number_field = Find(by=By.XPATH, value="//input[@id='administrator_address_1']")
    street_field = Find(by=By.XPATH, value="//input[@id='administrator_address_2']")
    city_field = Find(by=By.XPATH, value="//input[@id='administrator_city']")
    em_contact_field = Find(by=By.XPATH, value="//input[@id='emergency_contact']")
    em_phone_field = Find(by=By.XPATH, value="//input[@id='emergency_phone']")
    permission_entries = Finds(by=By.XPATH, value="//p[@ng-repeat='permission in vm.user.permissions']")
    permission_checkbox = Finds(by=By.XPATH, value="//input[@ng-model='permission.selected']")
    no_such_entry_msg = Find(by=By.XPATH, value="//td[@class='dataTables_empty']")
