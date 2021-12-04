import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from basics.chrome_launch import driver, url

url = "https://www.google.com"


class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get(url)
        print(driver.title)
        assert driver.title == "Google", f"Page title {driver.title} does not match with expected result"
        driver.get("https://accounts.google.com/")
        time.sleep(2)

    def test_enterEmail(self):
        # driver = self.driver
        login = driver.find_element_by_xpath("//input[@type='email']")
        login.send_keys("trunsingh1992@gmail.com")
        driver.find_element_by_xpath("//*[@id='identifierNext']/div/button").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//input[@name='password']").send_keys("447258singh")
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_id("idBtn_Back").send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='ShellMail_link']").send_keys(Keys.ENTER)
        print("herty")
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='id__7']")
        print("hi")
        time.sleep(5)

    # def test_logout(self):
    #   driver = self.driver
    #  driver.find_element_by_xpath("//*[@id=mectrl_main_body]")
    # time.sleep(5)

    # def tearDown(self):
        # driver = self.driver
    #     driver.quit()


if __name__ == '__main__':
    unittest.main()


