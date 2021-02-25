# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME(형식) - text/csv

import csv

# # 예제1
# with open('python_basic/resource/sample1.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader) #Header 스킵
#     # 확인
#     print(reader)
#     print(type(reader))
#     print(dir(reader))
#     print()

#     for c in reader:
#         print(c)

# # 예제2
# with open('python_basic/resource/sample2.csv', 'r') as f:
#     reader = csv.reader(f, delimiter='|') #delimiter 사용해서 구분자로 나누어줌 컴마가 아닌 다른 구분자로 되어있을 때 사용
#     next(reader) #Header 스킵
#     # 확인
#     print(reader)
#     print(type(reader))
#     print(dir(reader))
#     print()

#     for c in reader:
#         print(c)

# 예제3
with open('python_basic/resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print("------------------------")

# 예제4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

# newline 옵션을 이용해 한줄씩 쓸때 줄바꿈을 없앨수 있음
with open('python_basic/resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제5
with open('python_basic/resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)  # 한줄씩 쓰는게 아닌 한번에 쓰고싶을 때


# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl, xlrd)
# pip install xlrd
# pip install openpyxl
# pip install pandas
