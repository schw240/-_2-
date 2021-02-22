# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print("Hello Python!")
print('Hello Python!')
print("""Hello Python!""")
print('''Hello Python!''')

print()

# Separator 옵션 사용 (문자열을 원하는 문자로 연결해줌)
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용 (끝을 어떻게 할지 결정해줌, 넣으면 줄바꿈 안됨)
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

# end를 안넣으면 줄바꿈처리됨
print('test')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{a} are {b}'.format(a='You', b='Me'))

print()

# format을 사용하지 않고 쓰고싶다면 
# %s: 문자, %d: 정수, %f: 실수
print("%s's favourite number is %d" % ('Hanju', 7))

print("Test1: %5d, Price: %4.2f" % (776, 6543.123))
print('Test1: {0: 5d}, Price:{1: 4.2f}'.format(776, 6543.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6543.123))

'''
참고: Escape 코드
\n: 개행
\t: 탭
\\: 문자
\": 문자
\r: 캐리지 리턴
\f: 폼 피드
\a: 벨 소리
\b: 백 스페이스
\000: 널 문자
'''


print()
#따옴표 출력하고싶을 때
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\ttest')