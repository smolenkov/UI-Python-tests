import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from supplier.supplier import generated_person


class WebTablePage(BasePage):
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

    @allure.step('add new person')
    def add_new_person(self):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.ADD_BUTTON).click()
            self.element_is_visible(self.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.SUBMIT).click()
            count -= 1
            return [firstname, lastname, str(age), email, str(salary), department]

    @allure.step('check added people')
    def check_new_added_person(self):
        people_list = self.elements_are_present(self.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    @allure.step('find some person')
    def search_some_person(self, key_word):
        self.element_is_visible(self.SEARCH_INPUT).send_keys(key_word)

    @allure.step('check found person')
    def check_search_person(self):
        delete_button = self.element_is_present(self.DELETE_BUTTON)
        row = delete_button.find_element_by_xpath(self.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('update person information')
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.UPDATE_BUTTON).click()
        self.element_is_visible(self.AGE_INPUT).clear()
        self.element_is_visible(self.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.SUBMIT).click()
        return str(age)

    @allure.step('delete person')
    def delete_person(self):
        self.element_is_visible(self.DELETE_BUTTON).click()

    @allure.step('check deleted person')
    def check_deleted(self):
        return self.element_is_present(self.NO_ROWS_FOUND).text

    @allure.step('select up to some rows')
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_present(self.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('check count rows')
    def check_count_rows(self):
        list_rows = self.elements_are_present(self.FULL_PEOPLE_LIST)
        return len(list_rows)
