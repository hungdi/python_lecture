import socket
import time
import os

def client_without_finally():
    print(f"🐍 [PYTHON PID]: {os.getpid()}")
    print("❌ [WITHOUT FINALLY] 소켓 바깥에서 닫음 (예외 시 도달 안 함)")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(3)
        s.connect(("example.com", 80))  # 실제 열려 있음
        s.sendall(None)  # ❗ 일부러 예외 발생시킴 (TypeError)
    except ValueError:
        print("ValueError만 잡음 (TypeError는 못 잡음)")
    finally:
        time.sleep(30)

    # close를 해주었지만..
    # powershell에서 netstat -ano | findstr [pid]를 쳐봅시다.
    print("이런 케이스에 close엔 도달을 못해요")
    print("close를 안하면 무슨문제가 생길까?")
    s.close()


def client_with_finally():
    print("\n[WITH FINALLY] finally에서 무조건 닫음")

    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect(("example.com", 80))
        s.sendall(None)  # ❗ TypeError 발생
    except ValueError:
        print("ValueError만 잡음")  # TypeError는 못 잡음
    finally:
        if s:
            print("✅ finally에서 소켓 닫기")
            s.close()

    time.sleep(300)


# 하나만 주석 풀어서 실행
client_without_finally()
#client_with_finally()
