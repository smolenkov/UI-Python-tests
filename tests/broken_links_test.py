import allure

from pages.broken_links_page import BrokenLinksPage


@allure.feature('Links page')
class BrokenTestLinksPage:
    @allure.title('Checking the broken link')
    def test_broken_link(self, driver):
        broken_links_page = BrokenLinksPage(driver, 'https://demoqa.com/links')
        broken_links_page.open()
        response_code = broken_links_page.check_broken_link('https://demoqa.com/bad-request')
        assert response_code == 400, "the link works or the status code in son 400"
