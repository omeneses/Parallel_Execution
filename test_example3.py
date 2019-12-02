import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestExampleThreeClass:

    def test_1InputForm(self):

        print("Another example")
        mainMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Input Forms')]")
        mainMenu.click()

        subMenu = self.driver.find_element_by_xpath("//li/a[contains(text(), 'Simple Form Demo')]")
        subMenu.click()

        #Finding "Single input form" input text field by id. And sending keys(entering data) in it.
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
        print("I'm the test_funcfast")
        time.sleep(0.5)

    def test_3funcslow1(self):
        print("I'm the test_funcslow1")
        time.sleep(5)

    def test_4funcslow2(self):
        print("I'm the test_funcslow2")
        time.sleep(5)

    def test_5funcslow3(self):
        print("I'm the test_funcslow3")
        time.sleep(5)

    def test_6funcslow4(self):
        print("I'm the test_funcslow4")
        time.sleep(5)

    def test_7funcslow5(self):
        print("I'm the test_funcslow5")
        time.sleep(5)

    def test_8funcslow6(self):
        print("I'm the test_funcslow6")
        time.sleep(5)