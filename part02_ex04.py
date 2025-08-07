#part02_ex04.py
import datetime

# 목표 날짜 설정
target_date = datetime.date(2026, 1, 1)

# 오늘 날짜
today = datetime.date.today()

# 시간 차이 계산
time_delta = target_date - today
d_day = time_delta.days

print(f"새해까지 남은 날짜: D-{d_day}")