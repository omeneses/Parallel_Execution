import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExampleTwoClass:

    def test_1InputForm(self):

        print("Another example")
        mainMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Input Forms')]")
        mainMenu.click()

        subMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Simple Form Demo')]")
        subMenu.click()

        #Finding "Single input form" input text field by id. And sending keys(entering data) in it.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'user-message')))
        eleUserMessage = self.driver.find_element_by_id("user-message")
        eleUserMessage.clear()
        eleUserMessage.send_keys("Test Python")

        #Finding "Show Your Message" button element by css selector using both id and class name. And clicking it.
        eleShowMsgBtn=self.driver.find_element_by_css_selector('#get-input > .btn')
        eleShowMsgBtn.click()

        #Checking whether the input text and output text are same using assertion.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'display')))
        eleYourMsg=self.driver.find_element_by_id("display")
        assert "Test Python" in eleYourMsg.text

    def test_2funcfast(self):
        time.sleep(0.5)

    def test_3funcslow1(self):
        time.sleep(3)

    def test_4funcslow2(self):
        time.sleep(3)