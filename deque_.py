from collections import deque
import dis


def get():
    d = deque()
    d.append(3)
    d.append(4)



print(dis.dis(get))


# import collections
# import threading
# import time
# candle = collections.deque(range(5))
# def burn(direction, nextSource):
#  while True:
#   try:
#    next = nextSource()
#   except IndexError:
#    break
#   else:
#    print('%8s: %s' % (direction, next))
#    time.sleep(0.1)
#  print ('%8s done' % direction)
#  return
# left = threading.Thread(target=burn, args=('Left', candle.popleft))
# right = threading.Thread(target=burn, args=('Right', candle.pop))
# left.start()
# right.start()
# left.join()
# right.join()