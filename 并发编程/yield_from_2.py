#子生成器
def average_gen():
    total=0
    count=0
    average=0
    while True:
        new_num=yield average
        if new_num is None:
            break
        count+=1
        total+=new_num
        average=total/count
    return total,count,average


#委托生成器
def proxy_gen():
    while True:
        # 只有子生成器要结束（return）了，yield from左边的变量才会被赋值，后面的代码才会执行。
        total,count,average=yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))

def main():
    calc_average=proxy_gen()
    next(calc_average)
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))
    calc_average.send(None)
    calc_average.send(10)
    calc_average.send(None)
    # 如果此处再调用calc_average.send(10)，由于上一协程已经结束，将重开一协程

if __name__=="__main__":
    main()