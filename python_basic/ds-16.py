# 힙에 데이터 삭제 구현(Max Heap 예)
# 보통 삭제는 최상단 노드(root 노드)를 삭제하는 것이 일반적
# 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def moved_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array): # 전체 길이보다도 왼쪽 자식노드가 크다는건 말이 안됨 없다는 의미
            return False
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            # 자식이 더 크다면 바꿔주기
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # case3: 왼쪽 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]: # 왼쪽이 크다면
                # 부모노드와 비교
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # 부모보다 크다면
                    return True
                else:
                    return False
            else: # 오른쪽이 크다면
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]: # 오른쪽 노드가 부모보다 크다면
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1: # 데이터가 없는 경우
            return None
        
        returned_data = self.heap_array[1] #root node 반환
        self.heap_array[1] = self.heap_array[-1] # 마지막 노드를 루트노드로 올려줌
        del self.heap_array[-1]
        popped_idx = 1 # 추출된 데이터의 인덱스는 루트노드이기때문에 1부터 시작

        while self.moved_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # move_down에서 False인 경우는 고려하지 않음 조건문 밖으로 나가기 때문

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx

            # case3: 왼쪽 오른쪽 모두 있을 때
            else: 
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]: #left 경우
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else: # right 경우
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx
            

        return returned_data

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
        
        # 루트 노드 제거 후 가장 마지막 노드를 루트 노드로 지정
        # 루트 노드로 올라간 다음 자식노드랑 비교를 해야함


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.pop())
print(heap.heap_array)