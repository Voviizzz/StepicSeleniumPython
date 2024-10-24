import random
import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('NumberPromo', ['0','1','2','3','4','5','6',pytest.param('7', marks=pytest.mark.xfail),'8','9'])
def test_guest_can_go_to_login_page(browser, NumberPromo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{NumberPromo}"
    page = ProductPage(browser, link)
    page.open()
    # page.is_disappeared()
    # page.should_be_product_url()
    page.add_to_cart()
    page.solve_quiz_and_get_code()

# def test_guest_cant_see_success_message_after_adding_product_to_basket (browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.should_not_be_success_message()
# #
# def test_message_disappeared_after_adding_product_to_basket (browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_to_cart()
#     page.should_not_be_is_disappeared()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
# def test_guest_can_go_to_login_page_from_product_page (browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
def test_guest_cant_see_product_in_basket_opened_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_cart_page()
    page.should_not_be_products_in_cart()
    page.check_empty_cart_text()

# Класс для зарегестрированного пользователя
@pytest.mark.login
class TestUserAddToBasketFromProductPage ():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        from StepicSeleniumPython.pages.login_page import LoginPage
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(random.randint(11111111111, 44444444444444))
        page.register_new_user(email,password)
        page.should_be_authorized_user()

    # Как я понял, данный тест должен упасть
    @pytest.mark.xfail
    def test_user_cant_see_success_message (self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket (self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()

