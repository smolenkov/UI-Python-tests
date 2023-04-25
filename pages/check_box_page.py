import allure
import random
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckBoxPage(BasePage):
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

    @allure.step('open full list')
    def open_full_list(self):
        self.element_is_visible(self.EXPAND_ALL_BUTTON).click()

    @allure.step('click random items')
    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    @allure.step('get checked checkbox')
    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element_by_xpath(self.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('get output result')
    def get_output_result(self):
        result_list = self.elements_are_present(self.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
