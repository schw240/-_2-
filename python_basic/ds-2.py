import queue

data_queue = queue.LifoQueue()

# 데이터 입력
data_queue.put("funcoding")
data_queue.put(1)

# 큐 길이
print(data_queue.qsize())

# Dequeue LIFO 큐는 나중에 넣은 데이터 먼저 반환
print(data_queue.get())

print()
print()

# PriorityQueue() 만들기

data_queue = queue.PriorityQueue()

# 튜플 안 앞에있는 인자가 우선순위 값
# 숫자가 작을수록 우선순위가 높은것
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print(data_queue.qsize())

print(data_queue.get())