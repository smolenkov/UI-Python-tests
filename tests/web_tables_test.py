import random

import allure
from pages.web_tables_page import WebTablePage


@allure.feature('WebTable')
class TestWebTable:
    @allure.title('Сheck to add a person to the table')
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result

    @allure.title('Check human search in table')
    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, "the person was not found in the table"

    @allure.title('Checking to update the persons info in the table')
    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_some_person(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()
        assert age in row, "the person card has not been changed"

    @allure.title('Checking to remove a person from the table')
    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        web_table_page.search_some_person(email)
        web_table_page.delete_person()
        text = web_table_page.check_deleted()
        assert text == "No rows found"

    @allure.title('Check the change in the number of rows in the table')
    def test_web_table_change_count_row(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_up_to_some_rows()
        assert count == [5, 10, 20, 25, 50,
                         100], 'The number of rows in the table has not been changed or has changed incorrectly'
