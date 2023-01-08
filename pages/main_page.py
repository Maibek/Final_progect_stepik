import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    city = '//*[@id="main_area"]/div[1]/div/div[1]/a'
    catalog = '//*[@id="main_area"]/div[2]/div/div/div[2]/a[1]'
    search = '//*[@name="query"]'
    search_button = '//*[@id="main_area"]/div[2]/div/div/div[3]/div/div/div/form/input'
    login = '//*[@id="main_area"]/div[2]/div/div/div[4]/div[1]/a'
    cart = '//*[@id="main_area"]/div[2]/div/div/div[4]/div[4]/a'
    favorites = '//*[@id="main_area"]/div[2]/div/div/div[4]/div[3]/a'
    discounts = '//*[@id="main_area"]/div[2]/div/div/div[2]/a[2]'

    # Getters

    def get_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_search(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_favorites(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.favorites)))

    def get_discounts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.discounts)))

    # Action

    def search_city(self):
        print('Selected city ' + self.get_city().text)
        if self.get_city().text != 'Санкт-Петербург':
            self.get_city().click()
            time.sleep(2)
            self.driver.switch_to.window('//*[@id="popup_cityselectnew"]')
            selected_city = self.driver.element(By.XPATH, '//a[@title="Санкт-Петербург"]')
            """Не работает поиск элемента."""
            selected_city.click()
            print('Search city found')
            print('Selected city ' + selected_city.text)
        else:
            print('Search city error')

    def click_catalog(self):
        self.get_catalog().click()
        print('Click catalog button')

    def input_search(self, product):
        self.get_search().send_keys(product)
        print('Input search')

    def click_search_button(self):
        self.get_search_button().click()
        print('Click search button')

    def click_login(self):
        self.get_login().click()
        print('Click login button')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart button')

    def click_favorites(self):
        self.get_favorites().click()
        print('Click catalog button')

    def click_discounts(self):
        self.get_discounts().click()
        print('Click catalog button')

    # Methods

    def check_discounts(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.click_discounts()
        self.assert_url('https://www.onlinetrade.ru/actions/')
        self.screenshot('discounts')
