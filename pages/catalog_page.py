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

    # Getters

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

    # Action

    def click_electronics(self):
        self.get_electronics().click()
        print('Click electronics button')
        time.sleep(2)

    def click_computers(self):
        self.get_computers().click()
        print('Click computers button')
        time.sleep(2)

    def click_appliances(self):
        self.get_appliances().click()
        print('Click appliances button')
        time.sleep(2)

    def click_construction(self):
        self.get_construction().click()
        print('Click construction button')
        time.sleep(2)

    def click_goods(self):
        self.get_goods().click()
        print('Click goods button')
        time.sleep(2)

    def click_cottage(self):
        self.get_cottage().click()
        print('Click cottage button')
        time.sleep(2)

    def click_furniture(self):
        self.get_furniture().click()
        print('Click furniture button')
        time.sleep(2)

    def click_office(self):
        self.get_office().click()
        print('Click office button')
        time.sleep(2)

    def click_car(self):
        self.get_car().click()
        print('Click car button')
        time.sleep(2)

    def click_sport(self):
        self.get_sport().click()
        print('Click sport button')
        time.sleep(2)

    def click_beauty(self):
        self.get_beauty().click()
        print('Click beauty button')
        time.sleep(2)

    def click_children(self):
        self.get_children().click()
        print('Click children button')
        time.sleep(2)

    def click_pet(self):
        self.get_pet().click()
        print('Click pet button')
        time.sleep(2)

    def click_food(self):
        self.get_food().click()
        print('Click food button')
        time.sleep(2)

    def click_clothes(self):
        self.get_clothes().click()
        print('Click clothes button')
        time.sleep(2)

    def click_hobbies(self):
        self.get_hobbies().click()
        print('Click hobbies button')
        time.sleep(2)

    def click_watches(self):
        self.get_watches().click()
        print('Click watches button')
        time.sleep(2)

    def click_pharmacy(self):
        self.get_pharmacy().click()
        print('Click pharmacy button')
        time.sleep(2)

    def click_markdown(self):
        self.get_markdown().click()
        print('Click markdown button')
        time.sleep(2)

    def click_latest_arrivals(self):
        self.get_latest_arrivals().click()
        print('Click latest_arrivals button')
        time.sleep(2)

    # Methods

    def catalog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)

