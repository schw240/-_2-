# 해쉬 테이블
# 키에 데이터를 저장하는 데이터 구조
# 파이썬은 딕셔너리가 해쉬로 구현되어있으므로 별도로 구현할 필요없음

# 간단하게 hash table 구현하기

hash_table = list([0 for i in range(10)])
#print(hash_table)

# 간단한 해쉬함수
# 가장 간단한 방식인 Division 방법(나누기를 통한 나머지 값을 사용하는 기법)

def hash_func(key):
    return key % 5

# 해쉬 테이블에 저장해보기
# 데이터에 따라 필요시 key 생성 방법 정의
data1 = "Andy"
data2 = "Dave"
data3 = "Trump"

# ord(): 문자의 ASCII(아스키) 코드 리턴
print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
print(ord(data1[0]), hash_func(ord(data1[0])))

# 해쉬 테이블에 값 저장 예
# data:value 와 같이 data와 value를 넣으면 해당 data에 대한 key를
# 찾아서 해당 key에 대응하는 해쉬 주소에 value를 저장하는 예

def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value

# 실제 데이터를 저장하고 읽어보기
def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]
