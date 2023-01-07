import datetime


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
        print(get_url)
        print('URL value')

    """Проверка названия раздела"""

    def value_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Chapter "' + result + '" test OK')

    """Создание скриншота текущей страницы"""

    def screenshot(self, chapter):
        now_name = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = chapter + now_name + '.png'
        self.driver.execute_script("window.scrollBy(0, 200);")
        self.driver.save_screenshot('C:\\Testing\\Final project\\screen\\' + name_screenshot)