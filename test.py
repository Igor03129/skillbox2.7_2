
from selenium.webdriver import Remote
from selenium.webdriver.chromium import webdriver

driver = webdriver.Chrome()


class TestExample:
    def test_example(self):
        driver = Remote(command_executor="http://127.0.0.1:4444/wt/hub")
        driver.get("https://skillbox.ru")
        driver.quit()
