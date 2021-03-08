# 이진 탐색 트리 삭제

# 나누어서 생각해보기
# 5.4.1 Leaf Node 삭제
# Leaf Node: Child Node가 없는 Node
# 삭제할 Node의 Parent Node가 삭제할 Node를 가리키지 않도록 한다.
# 삭제할 Leaf Node를 삭제하고 연결되어있던 Branch를 None으로 만들면 됌


# 5.4.2 Child Node가 하나인 Node삭제
# 삭제할 Node의 Parent Node가 삭제할 Node의 Child Node를 가리키도록 한다.
# 삭제할 노드를 삭제하고 그 위의 Parent Node가 기존 노드에 연결되어있던 child Node를 가르키도록 함


# 5.4.3 Child Node가 2개인 Node 삭제
# 1. 삭제할 Node의 오른쪽 자식 중 가장 작은 값을 삭제할 Node의 Parent Node가 가르키도록 한다.
# 2. 삭제할 Node의 왼쪽 자식 중 가장 큰 값을 삭제할 Node의 Parent Node가 가르키도록 한다.
# 1,2 둘중 하나 사용
# 1번 시나리오
# 1. 삭제할 Node의 오른쪽 자식 선택
# 2. 오른쪽 자식의 가장 왼쪽에 있는 Node를 선택
# 3. 해당 Node를 삭제할 Node의 Parent Node의 왼쪽 Branch가 가르키게함
# 4. 해당 Node의 왼쪽 Branch가 삭제할 Node의 왼쪽 Child Node를 가르키게함
# 5. 해당 Node의 오른쪽 Branch가 삭제할 Node의 오른쪽 Child Node를 가르키게함
# 만약 해당 Node가 오른쪽 Child Node를 가직 있었을 경우에는 해당 Node의 본래 Parent Node의 왼쪽 Branch가 해당 오른쪽 Child Node를 가르키게함


# 코드 구현
# 삭제할 Node 탐색
# 삭제할 Node가 없는 경우도 처리해야함 이런경우 False 리턴 후 함수 종료

def delete(self, value):
    searched = False
    self.current_node = self.head  # 순회 위한 head 정하기
    self.parent = self.head
    # current_node는 삭제할 노드를 지칭하도록 할 예정
    # parent_node에는 삭제할 노드의 위에있는 노드를 지칭하도록 할 예정
    while self.current_node:
        if self.current_node.value == value:
            searched = True
            break
        elif value < self.current_node.value:  # 왼쪽에 있다면
            self.parent = self.current_node
            self.current_node = self.current_node.left
        else:
            self.parent = self.current_node
            self.current_node = self.current_node.right

    if searched == False:
        return False

    # 여기까지 왔을 떄 현재 current Node는 삭제할 노드
    # 그리고 parent는 current 노드의 parent 노드

    # 이후부터 Case들을 분리해서 코드 작성
    # 5.5.2 Case1: 삭제할 Node가 Leaf Node인 경우
    # self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:  # 리프노드인지 확인
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node  # 현재 노드 삭제(del 사용하면 메모리 상에서도 삭제)

    # Case2: 삭제할 Node가 Child Node를 한개 가지고 있을 경우
    if self.current_node.left != None and self.current_node.right == None:
        if value < self.parent.value:
            self.parent.left = self.current_node.left
        else:
            self.parent.right = self.current_node.left
    elif self.current_node.left == None and self.current_node.right != None:
        if value < self.parent.value:
            self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right

    if self.current_node.left != None and self.current_node.right != None:  # case3
        if value < self.parent.value:  # case3-1
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.left = self.change_node
            self.change_node.right = self.current_node.right
            self.change_node.left = self.change_node.left

        else:  # 3-2
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None
            self.parent.right = self.change_node
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
