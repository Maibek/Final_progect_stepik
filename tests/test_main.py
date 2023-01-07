import time
from selenium import webdriver

from pages.main_page import Main_page


def test_main():
    driver = webdriver.Chrome()

    print('Start test main')

    main = Main_page(driver)
    main.check_city()

    print('Stop test main')