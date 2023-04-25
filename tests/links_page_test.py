import allure
from pages.links_page import LinksPage


@allure.feature('Links page')
class TestLinksPage:
    @allure.title('Checking the link')
    def test_check_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "the link is broken or url is incorrect"
