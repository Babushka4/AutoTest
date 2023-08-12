from selenium.webdriver.common.by import By


class SearhTestLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, 'input#text')
    SUGGEST_BAR = (By.CSS_SELECTOR, 'li.mini-suggest__item.mini-suggest__item_type_fulltext.mini-suggest__item_arrow_yes.mini-suggest__item_with-button')
    FIRST_LINK = (By.CSS_SELECTOR, "a[class='Link Link_theme_normal OrganicTitle-Link organic__url link']")


class ImageTestLoactors:
    MENU_BUTTON = (By.CSS_SELECTOR, 'div.services-suggest__icons-more')
    IMAGE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="Картинки"]')
    CATEGORY_IMAGE = (By.XPATH, "//a[@class='Link PopularRequestList-Preview']")
    CATEGORY_TITLE = (By.CSS_SELECTOR, "div.PopularRequestList-SearchText")
    SEARCH_BAR = (By.CSS_SELECTOR, "input[name='text']")
    FIRST_IMAGE = (By.CSS_SELECTOR, "img.serp-item__thumb.justifier__thumb")
    FULL_SCREAN_IMAGE = (By.CSS_SELECTOR, "img.MMImage-Origin")
    NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, "div[class^='CircleButton CircleButton_type_next']")
    PREVIOUS_IMAGE_BUTTON = (By.CSS_SELECTOR, "div[class^='CircleButton CircleButton_type_prev']")
