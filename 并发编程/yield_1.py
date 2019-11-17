
def gen():
    i=0
    while i<5:
        temp=yield i
        print(temp)
        i+=1

f=gen()
next(f)
f.send("abc")
f.__next__()

