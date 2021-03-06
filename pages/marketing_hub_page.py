from selenium.webdriver.common.by import By
from webium import BasePage, Find


class MarketingHubPage(BasePage):

    groupon_button = Find(by=By.XPATH, value="//a[@href='integration_groupon.aspx']")
    
class DiscountPage(BasePage):
    
    url = 'https://ci004.godo.io/discount.aspx'    
