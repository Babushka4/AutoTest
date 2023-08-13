from locators.locators import ImageTestLoactors
from pages.CustomPages import ImagePage, SearchPage
from tests.BaseTest import BaseTest
import traceback


class TestImage(BaseTest):

    def test_image(self, driver):

        # подготовка формирования отчетности
        stage_list = ['Open page', 'Find menu button',
                      'Find image page button', 'Check current url',
                      'Choice the category', 'Search bar check',
                      'Image open check', 'Next image check',
                      'Previous image check']

        log_file, stage = self.get_log_tools(filename="image_test", stage_list=stage_list)

        # ТЕСТЫ
        try:
            page = SearchPage(driver)
            page.open('https://ya.ru')

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # проверка кнопки меню
            menu_but = page.check_menu_button()
            menu_but.click()

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # ищем ссылку на картинки
            page.get_image_button().click()
            driver.switch_to.window(driver.window_handles[-1])

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # проверка url
            assert driver.current_url == 'https://ya.ru/images/'

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # переопределяем класс страницы
            page = ImagePage(driver)

            # выбор категории
            target_title = page.find_element(ImageTestLoactors.CATEGORY_TITLE).text
            page.find_element(ImageTestLoactors.CATEGORY_IMAGE, time=10).click()

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # проверка поисковой строки
            current_title = page.find_element(ImageTestLoactors.SEARCH_BAR).get_attribute("value")
            assert target_title == current_title

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # проверка смены картинок
            page.find_element(ImageTestLoactors.FIRST_IMAGE).click()

            first_pic_src = page.find_element(ImageTestLoactors.FULL_SCREAN_IMAGE).get_attribute("src")
            log_file.write(f'Stage "{next(stage)}" finished.\n')
            page.next_image()

            second_pic_src = page.find_element(ImageTestLoactors.FULL_SCREAN_IMAGE).get_attribute("src")
            assert first_pic_src != second_pic_src
            log_file.write(f'Stage "{next(stage)}" finished.\n')

            page.previous_image()
            assert page.find_element(ImageTestLoactors.FULL_SCREAN_IMAGE).get_attribute("src") == first_pic_src

            log_file.write(f'Stage "{next(stage)}" finished.\n')
            log_file.write('\n---TEST FINISHED SUCCESS---')

        except:
            log_file.write(f'\nStage "{next(stage)}" FAILED WITH EXCEPTION:\n\n' + traceback.format_exc())

        finally:
            log_file.close()
