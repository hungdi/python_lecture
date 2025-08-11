import threading
import time

def worker(name):
    for i in range(3):
        print(f"{name} 작업 중... {i+1}")
        time.sleep(1)

# 스레드 생성
t1 = threading.Thread(target=worker, args=("스레드1",))
t2 = threading.Thread(target=worker, args=("스레드2",))

# 스레드 시작
t1.start()
t2.start()

# 메인스레드 기다림
t1.join()
t2.join()

print("모든 작업 완료")