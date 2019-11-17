from multiprocessing import Process


n=100

def work():
    global n
    n=0
    print("subprocess n is : %s" % n)


if __name__=="__main__":
    p=Process(target=work)
    p.start()
    print("mainprocess n is %s" %n)