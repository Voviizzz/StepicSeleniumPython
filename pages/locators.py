# 2. Внутри создайте новый класс. Каждый класс будет соответствовать каждому классу PageObject:

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_PAGE_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_USER_NAME = (By.NAME, "login-username")
    LOGIN_USER_PASSWORD = (By.NAME, "login-password")
    LOGIN_BUTTON_SBMT = (By.NAME, "login_submit")
#Форма регисрации
    REGISTRATION_USER_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_USER_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_USER_REPASSWORD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON_SBMT = (By.NAME, "registration_submit")

#Локаторы для продукта
class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    # SUCSESS_ADD_TO_CART_TEXT = ' был добавлен в вашу корзину'
    SUCSESS_ALLERT_ADD_TO_CART = (By.XPATH, "//*[@class='alertinner ' and text()[contains(.,' был добавлен в вашу корзину')]]")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    CART_LINK = (By.XPATH, "//*[@class='btn btn-default'][contains(text(),'Посмотреть')]")

    PRODUCTS_ON_CART = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_CART = (By.XPATH, "//*[@id='content_inner']//p [contains(text(),'Ваша корзина пуста')]")