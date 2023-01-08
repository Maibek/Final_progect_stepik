from selenium import webdriver

from pages.main_page import Main_page


def test_main():
    driver = webdriver.Chrome()

    main = Main_page(driver)
    main.check_discounts()
    driver.close()
