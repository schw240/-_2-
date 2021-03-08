# 트리 구조
# 트리: Node와 Branch를 이용해서 사이클을 이루지 않도록 구성한 데이터 구조
# 트리중 이진 트리(Binary Tree) 형태의 구조로, 탐색(검색) 알고리즘 구현을 위해 많이 사용됨

# 알아둘 용어
# Node: 트리에서 데이터를 저장하는 기본 요소(데이터와 다른 연결된 노드에 대한 Branch 정보 포함)
# Root Node: 트리 맨 위에 있는 노드
# Level: 최상위 노드를 Level 0 으로 하였을 때 하위 Branch로 연결된 노드의 깊이를 나타냄
# Parent Node: 어떤 노드의 다음 레벨에 연결된 노드
# Child Node: 어떤 노드의 상위 레벨에 연결된 노드
# Leaf Node(Terminal Node): Child Node가 하나도 없는 노드
# Sibling(Brother Node): 동일한 Parent Node를 가진 노드
# Depth: 트리에서 Node가 가질수 있는 최대 Level

# 이진 트리와 이진 탐색트리(Binary Search Tree)
# 이진 트리: 노드의 최대 Branch가 2인 트리
# 이진 탐색 트리(Binary Search Tree BST): 이진 트리에 다음과 같은 추가적인 조건이 있는 트리
#       왼쪽 노드는 해당 노드보다 작은 값, 오른쪽 노드는 해당 노드보다 큰 값을 가지고 있음




# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현
# 5.1 노드 클래스 만들기
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 5.2 이진 탐색 트리에 데이터 넣기
# 이진 탐색 트리 조건에 부합하게 넣어야함
class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value: # 새로 추가된 값이 기존 노드와 값을 비교했을때 작다면 왼쪽으로
                if self.current_node.left != None: #왼쪽으로 갔는데 이미 다른 노드가 있다면
                    self.current_node = self.current_node.left # 비교할 대상을 바꾸기 즉 왼쪽으로 갔을때 존재하는 노드를 current_node로 두기
                    # 이렇게 하면 while 반복문을 다시 돌면서 다시 비교
                else:
                    self.current_node.left = Node(value) # 노드가 없다면 연결시켜줌
                    break # 더이상 반복하지 않고 탈출
            else: # 작지 않다면(같은 경우도 마찬가지)
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

# 여기까지 이진 탐색 트리 구현 완료

    # 탐색 함수 (특정 데이터가 들어있는지 없는지 탐색)
    def search(self, value):
        self.current_node = self.head # 순회를 위해 헤드 먼저 설정
        while self.current_node: # 더이상 노드가 없다면 반복문 종료
            if self.current_node.value == value: # 현재 노드가 내가 찾는 노드인지 확인
                return True # 찾은 경우이므로 True 반환
            elif value < self.current_node.value: # 값이 현재 노드보다 작다면 왼쪽에 있음
                self.current_node = self.current_node.left #왼쪽으로 바꿔줌
            else: # 크다면
                self.current_node = self.current_node.right # 오른쪽으로 바꿔줌
        return False # 전부 돌았는데도 값이 없어서 반복문이 끝난 경우이므로 False 반환



# 테스트
head = Node(1) # 루트 노드는 강제로 만들기
BST = NodeMgmt(head) # 루트노드를 가지는 BST 객체 생성
BST.insert(2)
BST.insert(3)
BST.insert(0)
BST.insert(4)
BST.insert(8)
print(BST.search(-1))
