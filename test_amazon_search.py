import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestAmazon:
    search_words = ("lightsaber", "Dark side", "Obi one")

    driver = ""

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="/Users/iliapavlov/PycharmProjects/pytest/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")

    @pytest.mark.parametrize("search_query", search_words)
    def test_amazon_search(self, search_query):
        search = self.driver.find_element_by_id("twotabsearchtextbox")
        search.send_keys(search_query, Keys.ENTER)

        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element_by_xpath("//span[@class = 'a-color-state a-text-bold']").text

        assert expected_text == actual_text, f'Error. Expected text {expected_text}, but actual text: {actual_text}'

    def teardown_method(self):
        self.driver.close()
