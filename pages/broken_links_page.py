import allure
import requests
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BrokenLinksPage(BasePage):
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')

    @allure.step('check broken link')
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.BAD_REQUEST).click()
        else:
            return request.status_code
