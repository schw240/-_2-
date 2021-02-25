# Section09
# 파일 읽기, 쓰기
# 일기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a
# .. : 상대 경로, . : 절대 경로

# 파일 읽기
# 예제 1
f = open('python_basic/resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()


print("-----------------------------")

# 예제 2 with 문은 알아서 close을 해주므로 사용할 필요 없음
with open('python_basic/resource/review.txt', 'r') as f:
    c = f.read()
    #print(c)
    #print(list(c))
    print(iter(c))

print("-----------------------------")
print("-----------------------------")

# 예제 3
with open('python_basic/resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) # 한 라인씩 가져옴 strip 함수 사용하면 양쪽 공백을 제거해줌, 줄바꿈도 제거

print("-----------------------------")
print("-----------------------------")

# 예제 4
with open('python_basic/resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content) 

print("-----------------------------")
print("-----------------------------")

# 예제 5
with open('python_basic/resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' #### ')
        line = f.readline()

print()
print("-----------------------------")
print("-----------------------------")

# 예제 6
with open('python_basic/resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents) #리스트 형태로 가져옴
    for c in contents:
        print(c, end=' ***** ')

print()
print("-----------------------------")
print("-----------------------------")

# 예제 7
score = []

with open('python_basic/resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:.3}'.format(sum(score)/len(score)))


# 파일 쓰기

# 예제1
with open('python_basic/resource/text1.txt', 'w') as f:
    f.write("Niceman!\n")

# 예제2
with open('python_basic/resource/text1.txt', 'a') as f: #a는 추가
    f.write("Goodman!\n")

# 예제3
from random import randint

with open('python_basic/resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines: 리스트 -> 파일로 저장
with open('python_basic/resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)


# 예제5
with open('python_basic/resource/text4.txt', 'w') as f:
    print('Test Contents1!', file=f)
    print('Test Contents2!', file=f)