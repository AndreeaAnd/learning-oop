class Subject:
    def __init__(self):

        # cu _ pt a fi privata

        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class Observer:
    def __init__(self):
        pass

    def update(self, message):
        pass
    

