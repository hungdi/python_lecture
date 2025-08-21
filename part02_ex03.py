# part02_ex03.py
import time
from typing import ParamSpec, Callable, TypeVar

# 2. ParamSpec, TypeVar 정의
P = ParamSpec('P')
T = TypeVar('T')

# 데코레이터 작성
def measure_execution_time(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"함수 '{func.__name__}' 실행 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

# 데코레이터를 적용할 함수
@measure_execution_time
def long_running_task(sleep_time: int, name: str) -> str:
    print(f"{name} 작업을 {sleep_time}초 동안 실행합니다.")
    time.sleep(sleep_time)
    return f"작업 '{name}' 완료!"

# 실행구문
task_result = long_running_task(2, "데이터 처리")
print(task_result)

# 출력 결과:
# 데이터 처리 작업을 2초 동안 실행합니다.
# 함수 'long_running_task' 실행 시간: 2.00xx초
# 작업 '데이터 처리' 완료!