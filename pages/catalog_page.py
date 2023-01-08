import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Catalog_page(Base):
    url = 'https://www.onlinetrade.ru/catalogue/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    search_tv_name_product = 'Samsung'
    search_phone_name_product = 'Apple'

    # Locators

    electronics = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[1]/a'
    computers = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[2]/a'
    appliances = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[3]/a'
    construction = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[4]/a'
    goods = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[5]/a'
    cottage = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[6]/a'
    furniture = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[7]/a'
    office = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[8]/a'
    car = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[9]/a'
    sport = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[10]/a'
    beauty = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[11]/a'
    children = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[12]/a'
    pet = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[13]/a'
    food = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[14]/a'
    clothes = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[15]/a'
    hobbies = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[16]/a'
    watches = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[17]/a'
    pharmacy = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[18]/a'
    markdown = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[19]/a/div[2]'
    latest_arrivals = '//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[20]/a/div[2]'
    cart = '//*[@id="goods_content"]/div[1]/div[4]/div[2]/div[1]/div[3]/span/a'
    search_product = '//div[@class="indexGoods__item"]'
    value_world = '//*[@id="main_area"]/div[4]/div/h1'
    price_link = '//span[@itemprop="price"]'
    availadility = '//td[@title="Можно забрать"]'

    # Getters

    def get_value_world(self):
        return self.driver.find_element(By.XPATH, self.value_world)

    def get_electronics(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.electronics)))

    def get_computers(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.computers)))

    def get_appliances(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.appliances)))

    def get_construction(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.construction)))

    def get_goods(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.goods)))

    def get_cottage(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cottage)))

    def get_furniture(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.furniture)))

    def get_office(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.office)))

    def get_car(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.car)))

    def get_sport(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sport)))

    def get_beauty(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.beauty)))

    def get_children(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.children)))

    def get_pet(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pet)))

    def get_food(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.food)))

    def get_clothes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.clothes)))

    def get_hobbies(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.hobbies)))

    def get_watches(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.watches)))

    def get_pharmacy(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pharmacy)))

    def get_markdown(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.markdown)))

    def get_latest_arrivals(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.latest_arrivals)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_search_product(self, link):
        return self.driver.find_elements(By.XPATH, link)

    def get_price(self):
        return self.driver.find_element(By.XPATH, self.price_link)

    def get_availadility(self):
        return self.driver.find_elements(By.XPATH, self.availadility)

    # Action

    def click_electronics(self):
        self.get_electronics().click()
        print('Click electronics button')

    def click_computers(self):
        self.get_computers().click()
        print('Click computers button')

    def click_appliances(self):
        self.get_appliances().click()
        print('Click appliances button')

    def click_construction(self):
        self.get_construction().click()
        print('Click construction button')

    def click_goods(self):
        self.get_goods().click()
        print('Click goods button')

    def click_cottage(self):
        self.get_cottage().click()
        print('Click cottage button')

    def click_furniture(self):
        self.get_furniture().click()
        print('Click furniture button')

    def click_office(self):
        self.get_office().click()
        print('Click office button')

    def click_car(self):
        self.get_car().click()
        print('Click car button')

    def click_sport(self):
        self.get_sport().click()
        print('Click sport button')

    def click_beauty(self):
        self.get_beauty().click()
        print('Click beauty button')

    def click_children(self):
        self.get_children().click()
        print('Click children button')

    def click_pet(self):
        self.get_pet().click()
        print('Click pet button')

    def click_food(self):
        self.get_food().click()
        print('Click food button')

    def click_clothes(self):
        self.get_clothes().click()
        print('Click clothes button')

    def click_hobbies(self):
        self.get_hobbies().click()
        print('Click hobbies button')

    def click_watches(self):
        self.get_watches().click()
        print('Click watches button')

    def click_pharmacy(self):
        self.get_pharmacy().click()
        print('Click pharmacy button')

    def click_markdown(self):
        self.get_markdown().click()
        print('Click markdown button')

    def click_latest_arrivals(self):
        self.get_latest_arrivals().click()
        print('Click latest_arrivals button')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart button')

    def search_product_word(self):
        flag = True
        self.get_search_product(self.search_product)
        print('Number of products found: ' + str(len(self.get_search_product(self.search_product))))
        for i in range(1, len(self.get_search_product(self.search_product)) + 1):
            search_product = '//div[@class="indexGoods__item"][' + str(i) + ']'
            self.driver.find_element(By.XPATH, search_product)
            if self.search_tv_name_product.lower() in self.driver.find_element(By.XPATH, search_product).text.lower():
                flag = True
                continue
            else:
                print('Products do not match the filter')
                flag = False
                break

        if flag == True:
            print('All products match the filter')

    def value_tv(self):
        self.get_search_product(self.search_product)
        if len(self.get_search_product(self.search_product)) == 1:
            print('Filters product OK')
        else:
            print('Filters product ERROR')

    def value_availadility(self, link_argument, argument):
        self.get_search_product(link_argument)
        assert argument.lower() in self.driver.find_element(By.XPATH, self.availadility).text.lower()

    # Methods

    def product_tv_cart(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.click_electronics()
        self.filter_link('//*[@id="main_area"]/div[4]/div/div[4]/div/div[1]/div[1]/div[2]/ul/li[4]/a') #
        self.assert_url('https://www.onlinetrade.ru/catalogue/tv_i_video-c67/')
        self.value_word(self.get_value_world(), 'ТВ и Видео')
        self.filter_link('//a[@title="Телевизоры"]') #
        self.assert_url('https://www.onlinetrade.ru/catalogue/televizory-c181/')
        self.value_word(self.get_value_world(), 'Телевизоры')
        self.filter_link('//a[@title="' + self.search_tv_name_product.upper() + '"]')
        self.assert_url(
            'https://www.onlinetrade.ru/catalogue/televizory-c181/' + self.search_tv_name_product.lower() + '/')
        self.value_word(self.get_value_world(), 'Телевизоры ' + self.search_tv_name_product) # Выбор производителя телевизора
        print(len(self.get_search_product(self.search_product)))
        self.search_product_word()
        self.filter_link('//*[@id="l1d2185d7198ca866f057607628f90f1e"]') # Выбор доступности телевизора
        self.filter_link('//*[@id="l3984876a90c5a602e3aee832808551ca"]') # Выбор характеристик матрицы
        self.filter_link('//*[@id="l856595729b18bc1e9701ddeabd678b52"]') # Выбор диагонали
        time.sleep(2)
        self.filter_link('//a[@title="Подобрать"]')
        self.value_tv()
        price = self.get_price().text
        self.driver.find_element(By.XPATH, '//*[@id="item_container_2293371__ID"]/div[2]/a/div[1]/span[4]').click()
        assert price.replace(' ₽', '') == self.get_price().text # Проверка цены телевизора
        self.screenshot('price_tv')
        self.value_availadility(self.search_product, 'Сегодня') # Проверка доступности товара
        self.screenshot('club_price')
        self.filter_link('//*[@id="goods_content"]/div[1]/div[4]/div[2]/div[1]/div[3]/span/a')
        self.filter_link('//*[@id="popup_buy"]/div/div[1]/a')
        self.click_cart()
        self.filter_link('//*[@id="main_area"]/div[4]/div/div/div[2]/div/div/a[2]')
        self.value_word(self.driver.find_element(By.XPATH, '//*[@id="tabs_cart"]/div[1]/div[3]/div[1]/b'), price) # Проверка итоговой цены
        self.screenshot('finish_price')
