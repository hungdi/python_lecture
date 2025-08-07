try:
    my_list = [1, 2]
    print(my_list[3])
except Exception as e:
    print(e.args)

# 출력:
# 예외 발생: list index out of range
