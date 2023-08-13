from datetime import datetime
import os


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


class BaseTest:

    def get_log_tools(sellf, filename: str, stage_list: list):
        try:
            stage_iterator = iter(StageIterator(stage_list))

            if not os.path.exists('report/'):
                os.makedirs('report/')

            return open(f"report/{filename}_{datetime.now().date()}.txt", "w"), stage_iterator
        except:
            print('Creation log file failed')