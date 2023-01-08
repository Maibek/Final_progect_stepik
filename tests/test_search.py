from selenium import webdriver
from pages.search_page import Search_page


def test_search():
    driver = webdriver.Chrome()

    search = Search_page(driver)
    search.search_test()
    driver.close()