# 가변인자 순서 어길 시, 오류 확인
def func_test(**kwargs, *args, a, b):
    print(a, b, args, kwargs)
    pass

