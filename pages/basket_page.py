from StepicSeleniumPython.pages.base_page import *
from StepicSeleniumPython.pages.locators import *
# from selenium.webdriver.common.by import By
# from StepicSeleniumPython.pages.product_page import ProductPage


class BasketPage(BasePage):
    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCTS_ON_CART), \
            "В вашей корзине есть товар, но его быть не должно"

    def check_empty_cart_text(self):
        assert self.browser.find_element(*BasePageLocators.EMPTY_CART), 'Текста: "Ваша корзина пуста - нет"'

    # def should_not_be_cart_is_disappeared(self):
    #     assert self.is_disappeared(*BasePageLocators.EMPTY_CART), \
    #         "Сообщение о том, что корзина пустая не отобразилось"
    #
