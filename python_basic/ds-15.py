# 힙
# 힙(Heap) 이란
# 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)
# 완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

# 힙을 사용하는 이유:
# 배열에 데이터를 넣고 최대값과 최소값을 찾으려면 O(n)이 걸림
# 이에 반해 힙에 데이터를 넣고 최대값과 최소값을 찾으면 O(logn)이 걸림
# 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현등에 사용됨

# 힙의 구조
# 힙은 최대값을 구하기 위한 구조(최대 힙, Max Heap)와 최소값을 구하기 위한 구조(최소 힙, Min Heap)로 분류할 수 있음
# 힙은 다음과 같이 두가지 조건을 가지고 있는 자료구조
# 1. 각 노드의 해당 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다.(최대 힙의 경우)
# 최소 힙의 경우는 각 노드의 해당 자식 노드가 가진 값보다 크거나 작음
# 2. 완전 이진 트리 형태를 가짐

# 힙과 이진 탐색 트리의 공통점과 차이점
# 공통점: 힙과 이진 탐색 트리는 모두 이진트리임
# 차이점:
# 힙은 각 노드의 값이 자식 노드보다 크거나 같음(Max Heap의 경우)
# 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고 그 다음 부모노드, 그 다음 오른쪽 노드 값이 가장 큼
# 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은값은 왼쪽 큰 값은 오른쪽이라는 조건이 없음
#       힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클수도 있고 왼쪽이 클 수도 있음


# 힙 구현
# 힙은 일반적으로 배열 자료구조 활용해서 구현(완전 이진트리이기때문)
# 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면 구현이 수월
# 부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호(child node's index) // 2
# 왼쪽 자식 노드 인덱스 번호(left child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2
# 오른쪽 자식 노드 인덱스 번호(right child node's index) = 부모 노드 인덱스 번호(parent node's index) * 2 = 1

# Max Heap 데이터 삽입까지 클래스로 구현
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    # swap을 해야하는지 안하는지는 여기서 판단후 값 반환
    def move_up(self, inserted_idx):
        if inserted_idx <= 1: # 루트노드라면
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]: # 현재 노드가 부모보다 클때 스왑필요
            return True
        else:
            return False
        

    def insert(self, data):
        # 루트 노드가 없을 때
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        # 루트 노드가 아니라면 데이터 삽입
        # 데이터 추가하고 나서 부모노드와 비교하며 Swap
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array) - 1 # 전체 길이에서 -1 빼면 가장 끝 노드

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
