import time
from selenium import webdriver

from pages.discounts_page import Discounts_page
from pages.search_page import Search_page


def test_search():
    driver = webdriver.Chrome()

    print('Start test search')

    search = Search_page(driver)
    search.search_test()

    print('Stop test search')