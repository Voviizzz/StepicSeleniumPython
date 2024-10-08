
from StepicSeleniumPython.pages.base_page import BasePage
from .locators import  ProductPageLocators
from selenium.webdriver.common.by import By

# товарищ, который будет это проверять:
# test_user_can_add_product_to_basket
# test_guest_can_add_product_to_basket
# test_guest_cant_see_product_in_basket_opened_from_product_page
# test_guest_can_go_to_login_page_from_product_page
# данные методы есть, просто называны по-другому, не стал переименовывать, дабы не делать правки во всем проекте



class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCSESS_ALLERT_ADD_TO_CART), \
            "Success message is presented, but should not be"

    def should_not_be_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCSESS_ALLERT_ADD_TO_CART), \
            "Success message is presented, but disappeared not be"

    def add_to_cart(self):
        # self.should_be_product_url()
        self.click_add_to_cart()
        # self.solve_quiz_and_get_code()
        self.should_be_product_sucsess_add_book_name(
            self.get_book_name()
        )
        self.should_be_product_sucsess_add_book_price(
            self.get_book_price()
        )

    def get_book_name(self):
        book_name = self.browser.find_element(By.XPATH,"//*[@class='active'][1]").text
        return book_name

    def get_book_price(self):
        book_price = self.browser.find_element(By.XPATH,"//*[@class='col-sm-6 product_main']//*[@class='price_color']").text
        # print('цена книги', book_price)
        return book_price


    def click_add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        link.click()
        # self.should_be_product_sucsess_add()
        # return ProductPage(browser=self.browser, url=self.browser.current_url)

    def should_be_product_url(self):
        assert "?promo=" in self.browser.current_url, "Product is absent in current url"

    def should_be_product_sucsess_add_book_name(self, book_name):
        print(book_name)
        sucsees_add_to_cart = self.browser.find_element(By.XPATH, "//*[@class='alertinner ' and text()[contains(.,'добавлен в вашу корзину')]]")
        assert sucsees_add_to_cart.text == book_name +" был добавлен в вашу корзину.", "Продукт не был добавлен в корзину, есть отличие имен"

    def should_be_product_sucsess_add_book_price(self, book_price):
        print(book_price)
        cart_cost = self.browser.find_element(By.XPATH, "//*[@class='alertinner ']//p//strong").text
        assert cart_cost == book_price, "Стомость корзины отличается от стоимости товара"




