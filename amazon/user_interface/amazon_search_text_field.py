from screenpy import Target
from selenium.webdriver.common.by import By

SEARCH_INPUT = Target.the("Amazon search text field").located(By.ID, "twotabsearchtextbox")