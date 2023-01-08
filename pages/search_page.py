import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Search_page(Base):
    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    search_product = 'Samsung'
    search = '//*[@name="query"]'
    search_button = '//input[@class="header__search__inputGogogo"]'
    search_word = '//*[@id="main_area"]/div[4]/div/h1'
    search_value = '//div[@class="indexGoods__item"]'

    # Getters

    def get_search(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_search_word(self):
        return self.driver.find_element(By.XPATH, self.search_word)

    def get_search_value(self):
        return self.driver.find_elements(By.XPATH, self.search_value)

    # Action

    def input_search(self, product):
        self.get_search().send_keys(product)
        print('Input search')

    def click_search_button(self):
        self.get_search_button().click()
        print('Click search button')

    def search_value_word(self):
        flag = True
        self.get_search_value()
        print('Number of found items per page: ' + str(len(self.get_search_value())))
        for i in range(1, len(self.get_search_value()) + 1):
            search_value = '//div[@class="indexGoods__item"][' + str(i) + ']'
            self.driver.find_element(By.XPATH, search_value)
            if self.search_product.lower() in self.driver.find_element(By.XPATH, search_value).text.lower():
                flag = True
                continue
            else:
                print('Products do not match search results. Test ERROR')
                flag = False
                break

        if flag == True:
            print('All products match the search query')

    # Methods

    def search_test(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.input_search(self.search_product)
        self.click_search_button()
        self.search_value_word()
        self.assert_url('https://www.onlinetrade.ru/sitesearch.html?query=' + self.search_product)
        self.screenshot('search_test')
