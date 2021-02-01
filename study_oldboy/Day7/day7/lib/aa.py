__author__ = "Alex Li"

class C:

    def __init__(self):
        self.name = 'alex'

    def __call__(self, *args, **kwargs):
        print("runing call", args, kwargs)