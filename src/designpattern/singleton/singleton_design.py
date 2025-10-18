class Singleton:
    def __init__(self):
        self.instance = None

    def get_instance(self):
        if self.instance is None:
            instance = Singleton()
            return instance
    def hello(self):
        print("hello world")