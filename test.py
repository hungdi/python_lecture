fruits = ['apple', 'banana', 'melon']

fruits.append('orange') # 제일 뒤에 orange 추가
fruits.insert(1, 'kiwi') # 1번인덱스에 kiwi 추가

print(fruits)
print(fruits.index('banana'))
if 'banana' in fruits:
    print("banana가 있음")


fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()

print(fruits)

copy1 = fruits.copy()
combine_fruit = fruits + ['haha', 'zz']
print(combine_fruit)

###################################
# dictionary
###################################

person = {'name':'Lee', 'age':30}
person['job'] = 'engineer'

del person['job']
print(person)

age = person.pop('age')
print(person)
print(age)

print(person.keys())
print(person.values())
print(person.items())

print(person.get('hobby', 'No hobby'))
print(person.get('name'))
print(person)

person['job'] ='engineer'
person['age'] = 30

for key, value in person.items():
    print(f'{key}:{value}')


###################################
# 집합
###################################

nums = {1, 2, 3, 3, 2}

nums_empty = set()

nums.add(4)
#nums.remove(5) # 에러 발생
nums.discard(5) # 없어도 에러안남


set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)

if {1, 2} <= set1:
    print("포함하고있네요")


