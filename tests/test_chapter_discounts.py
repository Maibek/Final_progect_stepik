import time
from selenium import webdriver

from pages.discounts_page import Discounts_page


def test_chapter_discounts():
    driver = webdriver.Chrome()

    print('Start test chapter discounts')

    discount = Discounts_page(driver)
    discount.check_all_button()
    discount.check_discounts_product()
    discount.check_discounts_sets()
    discount.check_promo_codes()
    discount.check_gifts()
    discount.check_contests()
    discount.check_club_price()
    discount.check_other()
    discount.check_two_one()

    print('Test chapter discounts OK')
