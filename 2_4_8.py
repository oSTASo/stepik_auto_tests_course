import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    driver = webdriver.Chrome(executable_path="/Users/StanislavK/PycharmProjects/stepik/chromedriver")
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(url)

    WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    driver.find_element(By.CSS_SELECTOR, '#book').click()
    x = driver.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    driver.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    time.sleep(10)
    driver.quit()
