

class XYX:

    def __init__(self, *args, **kwargs):

        if len(args)==1:
            self._oneparm(*args, **kwargs)
        elif len(args)==2:
            self._twoparms(*args, **kwargs)
        else:
            print("weet niet")

    def _oneparm(self, a, b="c"):
        print(f"one {a}")

    def _twoparms(self, b, c, p = "he"):
        print(f"I want one more")


    def second(self, a):
        print("aaddd")

    def second(self, a, b ):
        print("bbaaaa")

    def third(self):
        print("third")

class X(XYX):
    print("aa")

    def second(self):
        print("bb")

class Z:
    print("z")


class Y(X, XYX):
    print("bbb")


c = XYX(2, 3)
a = XYX(1)

b = X(1)
b.second()
b.third()

c = Y(1)

