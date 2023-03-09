# 내장함수는 import가 필요없다.
# 대표적인 것만 살펴보며, 함께 메모해 드릴 인터넷 자료도 함께 참고하시면 좋겠습니다.

# 절대값
print(abs(-7))

# interable 객체의 모든 요소의 참/거짓을 판단
print(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(all([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(any([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# 객체가 가지는 변수나 함수를 표시
print(dir([1,2]))
print(dir({'chris' : 1, 'tommy' : 2}))

# 몫과 나머지를 튜플 형태로 반환
print(divmod(5, 2))

# 인덱스를 포함하는 enumerate 객체를 반환
for index, name in enumerate(['chris', 'tommy', 'harry']):
    print(index, name)

# 표현식을 실행하여 결과를 반환    
print(eval('1+4/2'))

# iterable 데이터를 리스트로 반환
data = list("Hello World")
print(data)

# iterable 데이터에 함수를 적용하여 반환
def multiple(x):
    return x*2

data = list(map(multiple, [1, 2, 3, 4, 5]))
print(data)

# 최대값 반환
print(max([1, 2, 3, 4, 5]))
# 최소값 반환
print(min([1, 2, 3, 4, 5]))

# 반올림
print(round(7.7))

# iterable 데이터를 정렬하여 반환
data = sorted("Hello World")
print(data)

# 데이터 타입을 반환
print(type(data))

# 데이터를 묶어서 반환
data = list(zip([1, 2, 3], ['a', 'b', 'c']))
print(data)