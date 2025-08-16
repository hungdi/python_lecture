# 가변 인자 예제
def sum_all(*args):
    return sum(args)

# 람다 + sorted 사용 예제
data = ['apple', 'banana', 'cherry']
sorted_data = sorted(data, key=lambda x: len(x))

# 클로저 예제
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

print(sum_all(1, 2, 3)) # 결과 6
print(sorted_data) # 문자열 길이에 따라 정렬된 결과를 반환
double = make_multiplier(2)
print(double(5))  # 결과: 10