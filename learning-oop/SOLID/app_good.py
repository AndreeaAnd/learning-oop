from abc import ABC, abstractmethod


class FrontEnd:
    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        data = self.data_source.get_data()
        print('Display data:', data)


class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

class Database(DataSource):
    def get_data(self):
        return 'Data from DB'

class API(DataSource):
    def get_data(self):
        return 'Data from API'

db_mysql=Database()
my_frontend_1=FrontEnd(db_mysql)
my_frontend_1.display_data()

api=API()
my_frontend_2=FrontEnd(api)
my_frontend_2.display_data()


