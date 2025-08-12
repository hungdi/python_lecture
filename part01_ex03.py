import pandas as pd

def load_csv(file_name):
    df = pd.read_csv(file_name)
    return df

def save_csv(df, file_name):
    df.to_csv(file_name, index=False, encoding="utf-8-sig")
    
def check_data(df):
    # '상품' 열만 선택
    product = df['상품']
    #print(product)

    # 여러 열 선택
    df_subset = df[['날짜', '상품', '단가']]
    #print(df_subset)

    print(df["상품"])          # 상품 열
    print(df[["상품", "수량"]]) # 여러 열
    print(df.loc[0])           # 첫 번째 행
    print(df.iloc[2, 3])       # 2행 3열 값

def check_data_basic_info(df):    
    # 상위 5행 / 하위 5행 미리보기
    print(df.head()) # 상위 5행 미리보기, 하위5행은 tail()
    print(df.shape) # 행 개수, 열 개수 (50, 7)
    print(df.info()) # 열 타입, 결측치 정보
    print(df.describe()) # 수치데이터 통계

def select_row_test(df):
    # 인덱스 이름 '0'에 해당하는 행 선택
    row_0 = df.loc[0]
    print("==== row_0 === ")
    print(row_0)

    # 정수 위치 '1'에 해당하는 행 선택
    row_1 = df.iloc[1]
    print("==== row_1 === ")
    print(row_1)

    # 여러 행 선택 (loc, iloc 모두 슬라이싱 가능)
    df_slice = df.iloc[0:2] # 첫 번째, 두 번째 행 선택
    print("==== df_slice === ")
    print(df_slice)

def filtered_data(df):
    # '수량'칼럼이 1500보다 큰 행만 선택
    df_filtered = df[df['수량'] > 5]
    print("==== df_filtered === ")
    print(df_filtered)

    # 여러 조건 결합 (AND: &, OR: |)
    df_multi_condition = df[(df['수량'] > 5) & (df['상품'] == 'B')]
    print("==== df_multi_condition (수량 5 초과, 상품은 B)=== ")
    print(df_multi_condition)

def preprocess_data(df):
    df_dropped = df.dropna()
    return df_dropped

# 상품이 A인 행에 대하여, 수량으로 내림차순
def add_column_and_filtering(df: pd.DataFrame):
    df = df.copy() # 원본을 변경하지않고 복사해서 씀.
    df["할인전총금액"] = df["수량"] * df["단가"]
    df_a = df[df["상품"] == "A"]

    # 수량 기준 내림차순 정렬
    df_sorted = df_a.sort_values(by="수량", ascending=False)
    return df_sorted

def grouping_data(df: pd.DataFrame):
    group_sum = df.groupby("상품")["총금액"].sum()
    print(group_sum)
    return group_sum

if __name__ == "__main__":
    input_file = "sample_sales_with_na.csv"
    output_file = "output_sales.csv"
    df = load_csv(input_file)
    df_dropped = preprocess_data(df)
    # check_data(df)
    df_filtered = add_column_and_filtering(df_dropped)
    # select_row_test(df)
    # filtered_data(df_dropped)
    df_group_sum = grouping_data(df_dropped)
    save_csv(df_group_sum, output_file)

    