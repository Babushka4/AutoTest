from selenium.webdriver import Keys
from locators.locators import SearhTestLocators
from pages.CustomPages import SearchPage, StageIterator
from datetime import datetime
import traceback
import os


class TestSearch:

    def test_search_bar(self, driver):
        # подготовка формирования отчетности
        stage_list = ['Open page', 'Find search bar',
                      '"Тензор" search', 'Suggest bar check',
                      'First link check']

        stage = iter(StageIterator(stage_list))

        if not os.path.exists('report/'):
            os.makedirs('report/')

        log_file = open(f"report/search_test_logs_{datetime.now().date()}.txt", "w")

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

            # проверка первой ссылки
            first_link = page.get_first_link()
            assert 'tensor.ru' in first_link.get_attribute("href")

            log_file.write(f'Stage "{next(stage)}" finished.\n')
            log_file.write('\n---TEST FINISHED SUCCESS---')

        except:
            log_file.write(f'\nStage "{next(stage)}" FAILED WITH EXCEPTION:\n\n' + traceback.format_exc())

        finally:
            log_file.close()
