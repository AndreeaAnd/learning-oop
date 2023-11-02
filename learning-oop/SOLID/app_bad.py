class Frontend:
    def __init__(self, back_end):
        self.back_end=back_end

    def display_data(self):
        data=self.back_end.get_data_from_db()
        print('Display data:', data)


class Backend:
    def get_data_from_db(self):
        return 'This is data from DB'
    