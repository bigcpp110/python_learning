from threading import Timer
import random



class Code():
    def __init__(self):
        self.make_cache()


    def make_cache(self,interval=3):
        self.cache=self.make_code()
        print(self.cache)
        self.t=Timer(interval,self.make_cache)
        self.t.start()


    def make_code(self,n=4):
        res=""
        for i  in range(n):
            s1=str(random.randint(0,9))
            s2=chr(random.randint(65,90)) # chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
            res+=random.choice([s1,s2])
        return res

    def check(self):
        while True:
            code=input("请输入您的而验证码>>:").strip()
            if code.upper()==self.cache:
                print("验证码正确")
                self.t.cancel()
                break

if __name__=="__main__":
    obj=Code()
    obj.check()