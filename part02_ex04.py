def my_map(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)

def my_map_list(func, *iterables):
    return [func(*args) for args in zip(*iterables)]

my_map_generator = my_map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])
print(next(my_map_generator))
print(next(my_map_generator))
print(next(my_map_generator))
print(my_map_list(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))


# generator는 아래 처럼 다양하게 사용가능
# 1. for문에서도 in 뒤에 generator가 나오면 자동으로 next()호출
for result_num in my_map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6]):
    print(result_num)

# 2. 그냥 list로 감싸서 출력하면, 내부적으로 next를 호출해서 값을 계산한다음 list에 저장
print(list(my_map(lambda x,y:x*y, [1, 2, 3], [4, 5, 6])))

