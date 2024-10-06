from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
# Это по POG
# т.к мы унаследуемся от base_page - передаывать browser нам не надо. Надо только self, ведь в констуркторе классе есть и browser и url и self
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

# def should_be_login_link(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"