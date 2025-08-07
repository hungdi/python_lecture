import datetime

# 현재 날짜 및 시간
now = datetime.datetime.now()

# 내 생일 설정
birthday = datetime.datetime(1990, 1, 10, 1, 30, 0)

# 두 시간의 차이를 계산하여 timedelta 객체 생성
time_left = now - birthday

# 결과 출력
print(f"내생일: {birthday.strftime('%Y년 %m월 %d일 %H시 %M분')}")
print(f"현재 시간: {now.strftime('%Y년 %m월 %d일 %H시 %M분')}")
print(f"태어난 후 얼마나 지났지?: {time_left.days}일, {time_left.seconds // 3600}시간, {(time_left.seconds % 3600) // 60}분")