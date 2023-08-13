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

    def check_menu_button(self):
        self.find_element(SearhTestLocators.SEARCH_BAR).click()
        return self.find_element(ImageTestLoactors.MENU_BUTTON)

    def get_image_button(self):
        return self.find_element(ImageTestLoactors.IMAGE_BUTTON)


class LinkListPage(BasePage):

    def get_first_link(self):
        return self.find_element(SearhTestLocators.FIRST_LINK)


class ImagePage(BasePage):

    def next_image(self):
        self.find_element(ImageTestLoactors.NEXT_IMAGE_BUTTON).click()

    def previous_image(self):
        self.find_element(ImageTestLoactors.PREVIOUS_IMAGE_BUTTON).click()



