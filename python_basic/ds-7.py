# 링크드 리스트(연결 리스트)
# 배열은 순차적으로 연결된 공간에 데이터를 나열하는 구조 (미리 크기 지정)
# 링크드 리스트는 떨어진 곳에 존대하는 데이터를 화살표로 연결해서 관리하는 데이터구조 (크기를 미리 지정X)
# C언어에서는 중요하나 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원

# 노드(Node): 데이터 저장 단위(데이터 값, 포인터) 로 구성
# 포인터(pointer): 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# 객체지향을 활용한 Node 구현 및 링크드 리스트 구현

# Node 구현
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
class Node:
    def __init__(self, data, next=None): # 주소까지 같이온다면 2번째 인자를  next에 넣어주고 data하나라면 다음 주소는 None라고 생각
        self.data = data                 # 즉 default값이 None라는 의미
        self.next = next

# Node와 Node 연결하기(포인터 활용)
node1 = Node(1)
node2 = Node(2)
# 여기까진 연결을 안시키고 객체만 만든상태(주소를 안넣었기 때문)

# 이부분에서 연결
node1.next = node2
# 맨 앞 노드를 head라고 지정
head = node1

# 링크드 리스트로 데이터 추가하기
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next: # 마지막 노드를 찾기위한 코드
        node = node.next
    # 마지막 노드를 찾았으므로 맨 뒤의 노드에다가 새로운 데이터(노드)를 추가
    node.next = Node(data)

node1 = Node(1)
head = node1

# 노드 추가
for index in range(1, 10):
    add(index)


# 추가된 데이터 출력하기(검색)
# node = head
# while node.next:
#     print(node.data)
#     node = node.next
# print(node.data)

# 새 노드 추가
node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next

node_next = node.next # 기존 다음 주소를 가르키고있던 노드를 node_next라는 새로운 변수에 저장
node.next = node3 # 새로만든 객체를 기존 노드의 다음으로 연결
node3.next = node_next # 새로 만든 객체의 다음값을 미리 만들어 두었던 다음주소와 연결