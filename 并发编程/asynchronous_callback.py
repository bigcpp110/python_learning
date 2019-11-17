from concurrent.futures import ThreadPoolExecutor
import time
import random


def la(name):
    print("%s is laing" % name)
    time.sleep(random.randint(3,5))
    res=random.randint(7,13)*"#"
    return {"name":name,"res":res}

def weigh(shit):
    shit=shit.result()
    name=shit["name"]
    size=len(shit["res"])
    print("%s 拉了 《%s》kg" % (name,size))


if __name__=="__main__":
    excutor=ThreadPoolExecutor(13)
    # shit1=excutor.submit(la,"alex").result()
    # weigh(shit1)
    # shit2 = excutor.submit(la, 'wupeiqi').result()
    # weigh(shit2)
    #
    # shit3 = excutor.submit(la, 'yuanhao').result()
    # weigh(shit3)

    excutor.submit(la, 'alex').add_done_callback(weigh)

    excutor.submit(la, 'wupeiqi').add_done_callback(weigh)

    excutor.submit(la, 'yuanhao').add_done_callback(weigh)
