from selenium.webdriver import Keys
from locators.locators import SearhTestLocators, ImageTestLoactors
from pages.base_page import BasePage


class SearchPage(BasePage):

    def get_search_bar(self, request_text=None):
        search_bar = self.find_element(SearhTestLocators.SEARCH_BAR)
        if request_text:
            search_bar.send_keys(request_text)
        return search_bar

    def suggest_bar_check(self):
        self.find_element(SearhTestLocators.SEARCH_BAR).send_keys()
        assert self.find_element(SearhTestLocators.SUGGEST_BAR)

    def get_first_link(self):
        return self.find_element(SearhTestLocators.FIRST_LINK)


class ImagePage(BasePage):

    def check_menu_button(self):
        self.find_element(SearhTestLocators.SEARCH_BAR).click()
        return self.find_element(ImageTestLoactors.MENU_BUTTON)


class StageIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value