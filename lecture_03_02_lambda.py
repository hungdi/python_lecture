# 기본함수 버전 v0
def square(x):
    return x ** 2

result = map(square, [1, 2, 3])
print(list(result))

# 람다 사용 예제 v1
result = map(lambda x: x**2, [1, 2, 3])
print(list(result))

# 람다 사용 예제 v2
# add 함수를 일반함수형태로 입력받아 출력해보고
# 람다 함수를 이용해서 출력해보기
a = int(input())
b = int(input())
 
def add(a, b):
    return a + b

print(add(a,b))
print((lambda a, b: a + b)(a,b))