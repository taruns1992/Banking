import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Testlogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.google.com")
        print(driver.title)
        assert driver.title == "Google", f"Page title {driver.title} does not match with expected result"
        driver.get("http://cookbook.seleniumacademy.com/Config.html")
        time.sleep(2)

    def test_checkbox_handling(self):
        element_LEDHeadLamp = driver.find_element_by_xpath("//input[@value='LEDHeadLamp']")
        print("hi")

        if not element_LEDHeadLamp.is_enabled():
            print("LEDHeadLamp checkbox disabled property is true")
        time.sleep(5)
        self.assertFalse(element_LEDHeadLamp.is_enabled())

    @classmethod
    def tearDownClass(cls):
        driver.quit()