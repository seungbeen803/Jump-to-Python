# 리스트의 수정과 삭제

# 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# del함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)