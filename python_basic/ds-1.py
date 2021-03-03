# 큐

import queue

# 일반적인 FIFO 정책의 큐
#queue가 라이브러리 명 Queue()가 클래스를 의미
data_queue = queue.Queue()

# 파이썬에서는 put, get 함수를 사용하여 Enqueue, Dequeue 구현
data_queue.put("funcoding")
data_queue.put(1)

# 큐 사이즈 확인하기
print(data_queue.qsize())

# Dequeue 첫번째 인자 출력
print(data_queue.get())
# Dequeue 두번째 인자 출력
print(data_queue.get())

# 큐 사이즈 확인하기
print(data_queue.qsize())
