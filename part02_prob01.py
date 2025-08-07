# part02_prob01.py
import random

# 1부터 45까지의 숫자를 담은 리스트 생성
numbers = list(range(1, 46))

# random.sample() 함수를 사용하여 중복 없이 6개 숫자 선택
lotto_numbers = random.sample(numbers, 6)

# 오름차순 정렬
lotto_numbers.sort()

# 결과 출력
print("로또 번호: ", lotto_numbers)