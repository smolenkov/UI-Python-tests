import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ButtonsPage(BasePage):
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    # result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    SUCCESS_RIGHT = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')

    @allure.step('click on different  buttons')
    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.SUCCESS_CLICK_ME)

    @allure.step('check clicked button')
    def check_clicked_on_the_button(self, element):
        return self.element_is_present(element).text
