from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
# link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"


# Это не по pageObjectModel - необходимо вынести переходы, логику в отдельные функции

# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

# # Это по POG
# def go_to_login_page(browser):
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()

# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                      # открываем страницу
#     page.go_to_login_page()
#
# def test_guest_should_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()