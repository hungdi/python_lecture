class CustomError(Exception):
    def __init__(self, message="음수 입력 오류가 발생했습니다."):
        #self.message = message
        super().__init__(message)
    

def my_function(value):
    if value < 10:
        raise CustomError()
    
try:
    my_function(-5)
except CustomError as e:
    print(e.args)
