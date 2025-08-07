#part02_ex03.py
import datetime

# 현재 날짜 및 시간 가져오기
now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now}")

# 특정 날짜 생성
my_birthday = datetime.date(1990, 5, 15)
print(f"내 생일: {my_birthday}")

# 날짜와 시간의 속성에 접근
print(f"년도: {now.year}, 월: {now.month}, 일: {now.day}")
print(f"시: {now.hour}, 분: {now.minute}, 초: {now.second}")