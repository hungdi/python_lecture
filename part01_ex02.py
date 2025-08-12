import pandas as pd

data = {
    '이름': ['철수', '영희', '민수'],
    '나이': [25, 30, 22],
    '도시': ['서울', '부산', '대구']
}
df = pd.DataFrame(data)
print(df)