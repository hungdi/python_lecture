import threading
import time

def background():
    for i in range(5):
        print(f"백그라운드 작업 {i+1}\n")
        time.sleep(1)
    
t = threading.Thread(target=background, daemon=True)
t.start()
print("메인 쓰레드 종료")
