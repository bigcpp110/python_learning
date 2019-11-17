from contextlib import contextmanager


@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()

with make_open_context("__class__.py","rb") as fp:
	data=fp.read()
	print(data)



@contextmanager
def make_open_context(filename, mode):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()

# with make_open_context('/tmp/a.txt', 'a') as file_obj:
#     file_obj.write("hello carson666")

# _*_ coding:utf-8 _*_


"""
contextmanager给了我们一个机会，即将原来不是上下文管理器的类变成了一个
上下文管理器，例如这里的MyResource类
"""
class MyResource:
    def query(self):
        print("query data")

@contextmanager
def make_myresource():
    print("connect to resource")
    yield MyResource()
    print("connect to resource")

with make_myresource() as r:
    r.query()	