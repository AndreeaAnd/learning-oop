from observable import Subject, Observer


class Event(Subject):
    pass


class EmailDelivery(Observer):

    def update(self, message):
        print(f'Sending email with {message}')


class PushNotification(Observer):

    def update(self, message):
        print(f'PushNotification with {message}')


class SMSNotification(Observer):

    def update(self, message):
        print(f'SMSNotification with {message}')