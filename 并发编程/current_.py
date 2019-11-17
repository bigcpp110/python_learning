from concurrent.futures import ThreadPoolExecutor,wait,as_completed
import requests


# with ThreadPoolExecutor(max_workers=1) as executor:
#     future=executor.submit(pow,2,2)
#     print(future.result())



#
# urls=['http://www.163.com', 'https://www.baidu.com/', 'https://github.com/']
#
# def load_url(url):
#     res=requests.get(url,timeout=60)
#     print("%r page is %d bytes" % (url,len(res.content)))
#
# executor=ThreadPoolExecutor(max_workers=3)
# f_list=[]
# for url in urls:
#     future=executor.submit(load_url,url)
#     f_list.append(future)

# print(wait(f_list))
# print("main process end")

# print(wait(f_list,return_when="FIRST_COMPLETED"))
# print("main process end")


from concurrent.futures import ThreadPoolExecutor
import requests
from functools import partial


def get(url):
    r=requests.get(url)
    return {"url":url,"text":r.text}


def parse(n,future):
    print("额外参数n: %s"%n)
    dic=future.result()
    print(dic)


if __name__=="__main__":
    executor=ThreadPoolExecutor()
    url_l = ['http://cn.bing.com/', 'http://www.cnblogs.com/wupeiqi/', 'http://www.cnblogs.com/654321cc/',
             'https://www.cnblogs.com/', 'http://society.people.com.cn/n1/2017/1012/c1008-29581930.html',
             'http://www.xilu.com/news/shaonianxinzangyou5gedong.html', ]
    futures=[]
    for url in url_l:
        executor.submit(get,url).add_done_callback(partial(parse,3))
    executor.shutdown()
    print("main process end")
