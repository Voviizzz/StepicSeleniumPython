from .base_page import BasePage
from .locators import  LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адре
        assert "/login" in self.browser.current_url, "login is absent in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME) and self.is_element_present(*LoginPageLocators.LOGIN_USER_PASSWORD), "Login form is not presented"

    #
    def should_be_register_form(self):
    # реализуйте проверку, что есть форма регистрации на странице
        assert (self.is_element_present(*LoginPageLocators.REGISTRATION_USER_EMAIL)
                and self.is_element_present(*LoginPageLocators.REGISTRATION_USER_REPASSWORD)
                    and self.is_element_present(*LoginPageLocators.REGISTRATION_USER_PASSWORD)
                         ), "Registration form is not presented"

    def  register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USER_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USER_REPASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON_SBMT).click()

