import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait

from basics.chrome_launch import driver, url

#url = "https://www.google.com"

class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.google.com")
        print(driver.title)
        assert driver.title == "Google", f"Page title {driver.title} does not match with expected result"
        driver.get("https://login.microsoftonline.com/")
        time.sleep(2)

    def test_enterEmail(self):
        # driver = self.driver
        login = driver.find_element_by_id("i0116")
        login.send_keys("tarun.singh1992@outlook.com")
        driver.find_element_by_id("idSIButton9").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//input[@name='passwd']").send_keys("447258S!ngh")
        driver.find_element_by_xpath("//input[@name='passwd']").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_id("idBtn_Back").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='ShellMail_link']").send_keys(Keys.ENTER)
        print("herty")
        time.sleep(50)
        #wait = WebDriverWait(driver, 20)
        #wait.until(expected_conditions.element_to_be_clickable((By.ID,"id__7")))
        new_message = driver.find_element_by_css_selector("#id__7")
        new_message.click()
        print("hi")
        time.sleep(3)

    #def test_logout(self):
     #   driver = self.driver
      #  driver.find_element_by_xpath("//*[@id=mectrl_main_body]")
       # time.sleep(5)

    def tearDownClass(cls):
        driver.quit()
        print("testcase executed ")

