import pytest
import time



@pytest.mark.usefixtures("setup")
class TestExample:
    def test_1title(self):
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    def test_2content_text(self):
        print("Verify content on the page...")
        centerText = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centerText
    def test_3funcfast(self):
        print("I'm the test_funcfast")
        time.sleep(0.5)

    def test_4funcslow1(self):
        print("I'm the test_funcslow1")
        time.sleep(5)

    def test_5funcslow2(self):
        print("I'm the test_funcslow2")
        time.sleep(5)

    def test_6funcfast(self):
        print("I'm the test_funcfast")
        time.sleep(0.5)

    def test_7funcslow1(self):
        print("I'm the test_funcslow1")
        time.sleep(5)

    def test_8funcslow2(self):
        print("I'm the test_funcslow2")
        time.sleep(5)

    def test_9funcfast(self):
        print("I'm the test_funcfast")
        time.sleep(0.5)

    def test_10funcslow1(self):
        print("I'm the test_funcslow1")
        time.sleep(5)

    def test_11funcslow2(self):
        print("I'm the test_funcslow2")
        time.sleep(5)