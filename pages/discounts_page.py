import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Discounts_page(Base):

    url = 'https://www.onlinetrade.ru/actions/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    discounts_word = '//*[@id="main_area"]/div[4]/div/div[4]/h1'
    all_button = '//a[@title="Все"]'
    discounts_product = '//a[@title="Скидки на товары"]'
    discounts_sets = '//a[@title="Скидки на комплекты"]'
    promo_codes = '//a[@title="Промокоды"]'
    gifts = '//a[@title="Подарки"]'
    contests = '//a[@title="Конкурсы"]'
    club_price = '//a[@title="Клубные цены"]'
    other = '//a[@title="Другое"]'
    two_one = '//a[@title="2+1"]'

    # Getters

    def get_discounts_word(self):
        return self.driver.find_element(By.XPATH, self.discounts_word)

    def get_all_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.all_button)))

    def get_discounts_product(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.discounts_product)))

    def get_discounts_sets(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.discounts_sets)))

    def get_promo_codes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.promo_codes)))

    def get_gifts(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.gifts)))

    def get_contests(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.contests)))

    def get_club_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.club_price)))

    def get_other(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.other)))

    def get_two_one(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.two_one)))

    # Action

    def click_all_button(self):
        self.get_all_button().click()
        print('Click all button')

    def click_discounts_product(self):
        self.get_discounts_product().click()
        print('Click discounts product button')

    def click_discounts_sets(self):
        self.get_discounts_sets().click()
        print('Click discounts sets button')

    def click_promo_codes(self):
        self.get_promo_codes().click()
        print('Click promo codes button')

    def click_gifts(self):
        self.get_gifts().click()
        print('Click gifts button')

    def click_contests(self):
        self.get_contests().click()
        print('Click contests button')

    def click_club_price(self):
        self.get_club_price().click()
        print('Click club price button')

    def click_other(self):
        self.get_other().click()
        print('Click other button')

    def click_two_one(self):
        self.get_two_one().click()
        print('Click 2+1 button')

    # Methods

    def check_all_button(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.click_all_button()
        self.value_word(self.get_discounts_word(), 'Акции')
        self.assert_url('https://www.onlinetrade.ru/actions/')
        self.screenshot('all_button')

    def check_discounts_product(self):
        self.click_discounts_product()
        self.value_word(self.get_discounts_word(), 'Скидки на товары')
        self.assert_url('https://www.onlinetrade.ru/actions/skidki_na_tovary.html')
        self.screenshot('discounts_product')

    def check_discounts_sets(self):
        self.click_discounts_sets()
        self.value_word(self.get_discounts_word(), 'Скидки на комплекты')
        self.assert_url('https://www.onlinetrade.ru/actions/skidki_na_komplekty.html')
        self.screenshot('discounts_product')

    def check_promo_codes(self):
        self.click_promo_codes()
        self.value_word(self.get_discounts_word(), 'Промокоды')
        self.assert_url('https://www.onlinetrade.ru/actions/promokody.html')
        self.screenshot('promo_codes')

    def check_gifts(self):
        self.click_gifts()
        self.value_word(self.get_discounts_word(), 'Подарки')
        self.assert_url('https://www.onlinetrade.ru/actions/podarki.html')
        self.screenshot('gifts')

    def check_contests(self):
        self.click_contests()
        self.value_word(self.get_discounts_word(), 'Конкурсы')
        self.assert_url('https://www.onlinetrade.ru/actions/konkursy.html')
        self.screenshot('contests')

    def check_club_price(self):
        self.click_club_price()
        self.value_word(self.get_discounts_word(), 'Клубные цены')
        self.assert_url('https://www.onlinetrade.ru/actions/klubnye_tseny.html')
        self.screenshot('club_price')

    def check_other(self):
        self.click_other()
        self.value_word(self.get_discounts_word(), 'Другое')
        self.assert_url('https://www.onlinetrade.ru/actions/drugoe.html')
        self.screenshot('other')

    def check_two_one(self):
        self.click_two_one()
        self.value_word(self.get_discounts_word(), '2+1')
        self.assert_url('https://www.onlinetrade.ru/actions/2_plus_1.html')
        self.screenshot('two_one')

