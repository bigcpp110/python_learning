from multiprocessing import Process,Queue

q=Queue(3)

q.put(1)
q.put(2)
q.put(3)
print(q.full())
print(q.get(1))

print(q.empty())