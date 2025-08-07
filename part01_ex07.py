import os

file = None
try:
    file = open("my_file.txt", "r")
    content = file.read()
    print(content)
    os._exit(0)    
except FileNotFoundError as e:
    print(e.args)
finally: # 무조건 실행됩니다. (try의 지역변수를 쓸 수 있습니다.)
    if file:
        file.close()
        print("파일을 닫았습니다")
