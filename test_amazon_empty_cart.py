from selenium import webdriver


class TestAmazonCart:
    driver = ""

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="/app_store/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")

    def test_empty_cart(self):
        element = self.driver.find_element_by_id("nav-cart-count-container")
        element.click()
        actual_text = self.driver.find_element_by_xpath("//div[@id = 'sc-active-cart']//h2").text
        expected_text = "Your Amazon Cart is empty"

        assert expected_text == actual_text, f"Error. Expected text '{expected_text}, but actual text: '{actual_text}"

    def teardown_method(self):
        self.driver.close()
