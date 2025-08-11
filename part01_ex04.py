import threading
import time

def background():
    for i in range(5):
        print(f"백그라운드 작업: {i}")
        time.sleep(0.5)
    print("백그라운드 쓰레드 종료")


t = threading.Thread(target=background, daemon=False)
t.start()
time.sleep(0.1)
print("메인 쓰레드 종료")

