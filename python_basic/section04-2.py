# Section04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = "NiceMan"
str3 = ''
str4 = str('ace')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_04 = 'Niceman'

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_04) #a가 str_04에 포함되어있는가?
print('z' not in str_04)
print('f' in str_04)


#문자열 형 변환
print(str(77) + 'a')
print(str(10.4))

#문자열 함수
a = 'niceman'
b = 'orange'

# print(a.islower())
# print(b.endswith('e'))
# print(a.capitalize())
# print(a.replace('nice', 'good'))
# print(list(reversed(b)))

print(a[0:3])
print(a[0:4])
print(a[0:7])
print(a[0:len(a)])
print(a[:])
print(a[:4])
print(b[0:4:2]) # 세번째 넣으면 세번째 수만큼 점프하면서 슬라이싱
print(b[1:-2])
print(b[::-1])

print()

a = 'abcdefg'
b = 'hhhhhhh'
#c = a[0] + b[0] + a[1] + b[1] + a[2] + b[2] + a[3] + b[3] + a[4]+ b[4] + a[5] 
c = a[i] + b[i] while len(c) < 11
print(c)