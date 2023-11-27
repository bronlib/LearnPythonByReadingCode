

print(f"\n\n******** Starting module {__file__} as {__name__} *************\n\n")

def tst0():

    def sim(x):
        print("starting sim")
        while x>0:
            x -= 1
            yield x

        print("finished loop")
        yield 101

    def sim2(x):
        yield x
        yield x+1
        yield 2
        yield 100

    for i in sim2(10):
        print(str(i))
        if i == 2:
            break

    # bb = [i for i in sim2(2)]
    # print(str(bb))


def tst1():

    def sim(a):

        print(f"State 0 a={a}")
        b = yield a
        print("input value a=",a," received b ",b)
        c = yield b
        print("input value a=", a, " received c ", c ," b ",b)
        f = yield c



    gen = sim(11)
    print("starting ", str(next(gen)))
    print("sending 20 and received: ",gen.send(20))
    print("sending 3 and received: ",gen.send(3))

    print("\n-----starting for for loop ")

    for i in sim(1):
        print("In For loop ",str(i))




def tst2():

    def sim():
        print("State 0")
        b = yield 1
        print("received b ", b)
        c = yield 2
        print("received c ", c)
        f = yield 3

    for i in sim():
        print("In For loop ", str(i))


def tst3():
    """
    there is as clear need for "start" and "end"
    all inbetween works
    So it must start with a next, whose output can be used for
    initialization.

    :return:
    """
    def ex2(nr):
        x = 10
        for i in range(nr):
            print("before yield # ",i," value ", x)
            x = yield (x+1)
            print("recevied # ",i," value ",x)

        print("loop in ex done now x is ",x)
        yield x # now both can be just as long


    nr = 4
    gen = ex2(nr)  # nr+1 is the number of transactions
    a = next(gen)  # go to the first yield
    for i in range(nr):
        tosend = a
        print("sending # ",i," value ",tosend)
        # this sends a value of the previous yield and receives the value of the next yield
        a = gen.send(tosend)
        print("from send ", a)

    print("Finished ")


"""
Python also has many powerful standard functions. 
locals() returns a dictionary representing the current local symbol table.
For methods, like tst0 above, it means that the name of the method is in 
string form as a key. As a key it can now be executed by: locals()["tst0"]()
To be clear, the part locals()["tst0"] is a pointer to the function and by adding the brackets (), it is called.
"""
for i in [0,1,2]:
   locals()[f"tst{i}"]()

print(f"\n\n******** Ending module {__file__} as {__name__} *************\n\n")