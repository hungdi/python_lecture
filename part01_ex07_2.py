try:
    raise ValueError
except TypeError as e:
    print(e.args)
finally:
    print("여기는 실행됩니다.")

print("여기는 실행되지않아요.")