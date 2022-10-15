#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math
import time

URL = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(URL)

    WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "h5#price"), "${}".format(100)
        )
    )

    book_button = browser.find_element(By.CSS_SELECTOR, "button#book")
    book_button.click()

    x = int(browser.find_element(By.CSS_SELECTOR, "span#input_value").text)
    print("x = {}".format(x))

    y = calc(x)
    print("y = {}".format(y))

    y_input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    y_input.send_keys(str(y))

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    time.sleep(10)
except:
    raise

finally:
    browser.quit()
