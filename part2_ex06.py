def list_eq(a: list, b: list) -> bool:
    if len(a) != len(b):
        return False
    for x, y in zip(a,b):
        if x != y:
            return False
    
    return True

print(list_eq(list([1,2,3]), list([1,2,3])))
