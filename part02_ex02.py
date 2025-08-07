#part02_ex02.py
import random

# 0.0 ~ 1.0 사이의 난수
print(f"무작위 실수: {random.random()}")

# 1 ~ 100 사이의 정수 난수
print(f"1부터 100까지의 무작위 정수: {random.randint(1, 100)}")

# 리스트에서 무작위 요소 선택
fruits = ['사과', '바나나', '체리', '딸기']
print(f"오늘의 과일 추천: {random.choice(fruits)}")

# 리스트의 순서 섞기
my_numbers = [1, 2, 3, 4, 5]
print(f"섞기 전 리스트: {my_numbers}")
random.shuffle(my_numbers)
print(f"섞은 후 리스트: {my_numbers}")

