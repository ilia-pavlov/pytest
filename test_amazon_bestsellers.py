from selenium import webdriver


class TestAmazonBestsellers:
    driver = ""

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="/app_store/chromedriver")
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.amazon.com/")

    def test_amazon_bestsellers_links(self):
        self.driver.find_element_by_xpath("//div[@id = 'nav-xshop']/a[contains(@href, 'bestseller')]").click()
        actual_links = self.driver.find_elements_by_xpath("//div[@id = 'zg_tabs']//li")
        assert len(actual_links) == 5, f"Expected to see 5 bestseller links, got {len(actual_links)}"

    def teardown_method(self):
        self.driver.close()
