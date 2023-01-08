import time

from selenium import webdriver
from pages.catalog_page import Catalog_page


def test_cart():
    driver = webdriver.Chrome()

    cart = Catalog_page(driver)
    cart.product_tv_cart()
    driver.close()