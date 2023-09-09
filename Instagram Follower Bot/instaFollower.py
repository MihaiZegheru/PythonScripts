from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
import random


class InstaFollower:
    CHROME_PATH = ""

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=self.CHROME_PATH)

    def login(self, email, password):
        print("login")
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)

        try:
            accept_cookie_button = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
            accept_cookie_button.click()
        except NoSuchElementException:
            pass

        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(email)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.submit()
        sleep(2)

    def find_followers(self):
        print("find")
        self.driver.get("https://www.instagram.com/nike")
        sleep(2)

        followers_button = self.driver.find_element_by_xpath('/html/body/div[1]/section/main'
                                                             '/div/header/section/ul/li[2]/a')
        followers_button.click()
        sleep(2)

        # while True:
        #     element = self.driver.find_element_by_class_name("wo9IH")
        #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
        #     sleep(2)
        modal = self.driver.find_element_by_css_selector('.isgrP')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        print("follow")
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(random.randrange(4, 6))
                if random.randint(1, 20) is 1:
                    sleep(15)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()
