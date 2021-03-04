# 파이썬 객체지향 프로그래밍으로 링크드 리스트 구현하기

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            print('해당 값을 가진 노드가 없습니다.')
            return
        # head 삭제 경우
        if self.head.data == data:
            temp = self.head  #head를 임시 변수 temp에 넣음
            self.head = self.head.next # head에 head의 다음값을 넣음
            del temp # 해당 객체 (head) 삭제
        # 2,3번 마지막 노드와 중간 노드삭제의 경우
        else:
            # 헤드의 데이터 삭제가 아닌경우
            node = self.head
            while node.next:
                #head다음부터의 데이터가 data인지 확인
                if node.next.data == data:
                    temp = node.next
                    # 만약 중간 데이터가 삭제할 데이터라면 기존 노드의 다음을 temp에 저장하고
                    # 다음다음 데이터를 기존 노드에 연결
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next

            

#linkedlist1 = NodeMgmt(0)
#linkedlist1.desc()

# 데이터 추가
# for data in range(1, 10):
#     linkedlist1.add(data)
# linkedlist1.desc()

# 데이터 삭제
linkedlist1 = NodeMgmt(0)
for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()
linkedlist1.delete(4)
print('-'*20)
linkedlist1.desc()