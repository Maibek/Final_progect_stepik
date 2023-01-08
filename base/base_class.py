import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Получение текущего url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    """Проверка текущего url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('URL value ' + get_url)

    """Проверка названия раздела"""

    def value_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word.lower() == result.lower()
        print('Chapter "' + result)

    """Создание скриншота текущей страницы"""

    def screenshot(self, chapter):
        now_name = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = chapter + now_name + '.png'
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.driver.save_screenshot('C:\\Testing\\Final project\\screen\\' + name_screenshot)

    def filter_link(self, filter):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, filter))).click()