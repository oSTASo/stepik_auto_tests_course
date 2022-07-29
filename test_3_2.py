import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):
    def test_1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome(executable_path="/Users/StanislavK/PycharmProjects/stepik/chromedriver")
        browser.get(link)
        input = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input.send_keys("Ivan")
        input = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input.send_keys("Ivan")
        input = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input.send_keys("Ivan")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'OKI')

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome(executable_path="/Users/StanislavK/PycharmProjects/stepik/chromedriver")
        browser.get(link)
        input = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
        input.send_keys("Ivan")
        input = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
        input.send_keys("Ivan")
        input = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
        input.send_keys("Ivan")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(3)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'OKI')


if __name__ == "__main__":
    unittest.main()
