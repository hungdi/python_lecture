fruits = ['apple', 'banana', 'cherry']
print(fruits)
fruits.append('orange')
print(fruits)
fruits.insert(1, 'grape')
print(fruits)
#fruits.remove('banana')
fruits.pop()
print(fruits)
fruits.append(3)
print(fruits)
fruits.append(True)
print(fruits)

# 검색 확인
print('apple' in fruits)
if 'apple' in fruits :
    print ("apple이 있습니다")

print(fruits.index('banana'))
if fruits.index('banana') == 2:
    print(f"banana의 index는 {fruits.index('banana')} 입니다")

print(fruits)
fruits.remove(True)
fruits.remove(3)
fruits.sort(reverse=True)
print(fruits)
fruits.reverse()
print(fruits)

fruits_copy = fruits.copy()
new_fruits = ['mango', 'kiwi']
combine_list = fruits + new_fruits
print(combine_list)


person = {'name':'Alice', 'age':30}
person['job'] = 'Engineer'
del person['age']
print(person)
job = person.pop('job')
print(job)
print(person)
person['job'] = 'Manager'
person['age'] = 35
print(person)
del person['age']
print(person)

for key, value in person.items():
    print(f'{key}:{value}')

for item in fruits:
    print(f'{item}')

print(person.keys())
print(person.values())
print(person.items())

print(person.get('hobby', 'No hobby')) # 키값이 없으면, No hobby 출력
print(person.get('job', 'no job'))


nums = {'a', 'b', 'c', 'a', 'a'}
print(nums)
nums.add('b')
print(nums)

#nums.remove('a')
nums.discard('z')
print(nums)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2) 
print(set1 & set2) 
print(set1 - set2) #차집합
print(set1 ^ set2) #합집합 - 교집합

print({1,2} <= set1)
