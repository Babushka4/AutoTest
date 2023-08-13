from selenium.webdriver import Keys
from locators.locators import SearhTestLocators
from pages.CustomPages import SearchPage, LinkListPage
from tests.BaseTest import BaseTest
import traceback


class TestSearch(BaseTest):

    def test_search_bar(self, driver):
        # подготовка формирования отчетности
        stage_list = ['Open page', 'Find search bar',
                      '"Тензор" search', 'Suggest bar check',
                      'First link check']

        log_file, stage = self.get_log_tools(filename="search_test", stage_list=stage_list)

        # ТЕСТЫ
        try:
            page = SearchPage(driver)
            page.open('https://ya.ru')

            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # проверка наличия строки поиска
            page.find_element(SearhTestLocators.SEARCH_BAR)
            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # ввод в строку поиска "Tensor"
            search_bar = page.get_search_bar('Тензор')
            log_file.write(f'Stage "{next(stage)}" finished.\n')

            # проверка появиласл ли подсказка
            page.suggest_bar_check()
            log_file.write(f'Stage "{next(stage)}" finished.\n')

            search_bar.send_keys(Keys.ENTER)

            # переопределяем актуальную страницу
            page = LinkListPage(driver)

            # проверка первой ссылки
            first_link = page.get_first_link()
            assert 'tensor.ru' in first_link.get_attribute("href")

            log_file.write(f'Stage "{next(stage)}" finished.\n')
            log_file.write('\n---TEST FINISHED SUCCESS---')

        except:
            log_file.write(f'\nStage "{next(stage)}" FAILED WITH EXCEPTION:\n\n' + traceback.format_exc())

        finally:
            log_file.close()
