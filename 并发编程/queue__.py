import queue


# 先进先出
q=queue.Queue(3)  # 设置最大容量

q.put('first')
q.put(2)
q.put('third')

print(q.get())
print(q.get())
print(q.get())


#后进先出
q=queue.LifoQueue(3)
q.put('first')
q.put(2)
q.put('third')

print(q.get())
print(q.get())
print(q.get())


#优先级队列 值越小先出
q = queue.PriorityQueue(3)  # 优先级队列

q.put((10, 'one'))
q.put((40, 'two'))
q.put((30, 'three'))

print(q.get())
print(q.get())
print(q.get())

