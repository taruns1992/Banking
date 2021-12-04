import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.google.com")
        print(driver.title)
        assert driver.title == "Google", f"Page title {driver.title} does not match with expected result"
        driver.get("https://login.yahoo.com/")
        time.sleep(2)

    def test_enterEmail(self):
        login = driver.find_element_by_id("login-username")
        login.send_keys("tarun_singh1991@yahoo.com")
        driver.find_element_by_id("login-signin").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_id("login-passwd").send_keys("447258S!ngh")
        driver.find_element_by_xpath("//*[@id='login-signin']").send_keys(Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='ymail']/div").click()
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/nav/div/div[1]/a").send_keys(Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_id("message-to-field").send_keys("trunsingh1992@gmail.com")
        print("to email")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@placeholder='Subject']").send_keys("My first automation email")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='editor-container']/div[1]").send_keys("First email send through automation script")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='mail-app-component']/div/div/div[2]/div[2]/div/button").send_keys(Keys.ENTER)
        time.sleep(5)

    def test_logout(self):
        driver.find_element_by_xpath("//*[@id='ybarAccountMenuOpener']/div/img").click()
        time.sleep(5)
        print("Hi logout")

    @classmethod
    def tearDownClass(cls):
        driver.quit()
        print("testcase executed ")