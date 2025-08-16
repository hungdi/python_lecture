def make_moving_average(n):
    avrg = []
    def ma(x):
        if len(avrg) >= 3:
            avrg.pop(0) # 오래된 요소 제거
        
        avrg.append(x)
        print(avrg)
        return sum(avrg)/len(avrg)
    return ma
    
ma = make_moving_average(3)
print(ma(10))
print(ma(20))
print(ma(30))
print(ma(40))


