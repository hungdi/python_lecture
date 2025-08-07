try:
    int("abc")
except ValueError as e:
    print("예외 클래스:", type(e))       # <class 'ValueError'>
    print("에러 메시지:", str(e))        # invalid literal for int() with base 10: 'abc'
    print("args 내용:", e.args)         # ('invalid literal for int() with base 10: \'abc\'',)
