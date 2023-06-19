
class CanBeCalled():

    def __init__(self):
        self.dynamic_variable = 10

    def show_locals(self):
        print("locals in this object {}".format(vars(self)))


def function_local():
    print("calling function in module {}".format(__name__))