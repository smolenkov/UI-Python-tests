import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RadioButtonPage(BasePage):
    YES_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')

    @allure.step('click on the radiobutton')
    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.YES_RADIOBUTTON,
                   'impressive': self.IMPRESSIVE_RADIOBUTTON,
                   'no': self.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    @allure.step('get output result')
    def get_output_result(self):
        return self.element_is_present(self.OUTPUT_RESULT).text
