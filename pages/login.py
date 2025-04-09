from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from testdata.login_page_data import vars

class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def launch_website(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)
       
    def user_creds(self,username,password):
        try:
            self.driver.find_element(By.ID,"username").send_keys(username)
            self.driver.find_element(By.ID,"password").send_keys(password)
            self.driver.find_element(By.ID,"Login").click()
            self.driver.implicitly_wait(5)
            return 1
        except Exception as e:
            print(f"login error: {e}")
            return 0          

    def page_title(self):
        actual_title = self.driver.title
        expected_title =  "Home | Salesforce"
        if actual_title == expected_title:
            return 1
        else:
            print(f"title mismatch! Expected title: {expected_title}, Got: {actual_title}")
            return 0

