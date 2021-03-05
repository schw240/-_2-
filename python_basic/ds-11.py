# 리스트 변수 활용해서 해쉬 테이블 구현해보기

hash_table = list([0 for i in range(8)])

def get_key(data):
    return hash(data) # 해쉬 키 생성

def hash_function(key):
    return key % 8

def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value

def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]

save_data('Dave', '0102030200')
save_data('Andy', '01033232200')
print(read_data('Dave'))
print(hash_table)