

print(f"\n\n******** starting module {__file__} as {__name__} *************\n\n")
def justone(aa):

    print("staring aa")
    if aa>0:
        b = yield aa
        print("going again"," recevied: ",str(b))
        yield 2
        print("after 2")
        yield 3
        print("ended after 3")



gen = justone(2)
print("started ")
print(gen)
print("looking at gen")
# must first call next before sending it something print("first calling send ",gen.send(20))
print("calling ", next(gen))
gen.send(20)
print("sent 20")
print("Last time ",next(gen))
try:
   next(gen)
except:
    print("Finished ")


print("\n\n Now Viewing the generator as loop")
gen = justone(2)
for i in gen:
    print(i)



print(f"\n\n******** Ending module {__file__} as {__name__} *************\n\n")