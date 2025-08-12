import pandas as pd

def read_file(filename):
    df = pd.read_csv(filename)
    return df

def q4_max(df: pd.DataFrame):
    # 지역별 최고 PM10 계산
    print("=========q4==========")
    df_max = df.groupby('지역')[df.columns[2]].max().reset_index()
    print(df_max)

def q5_dropna_average(df: pd.DataFrame):
    print("=========q5==========")
    df_dropped = df.dropna().copy()
    df_sorted = df_dropped.groupby('연도')[df.columns[3]].mean().reset_index().sort_values("연도", ascending=False)
    print(df_sorted)

def q6_topn(df: pd.DataFrame):
    print("=========q6==========")
    df_sorted = df[df['연도'] == 2015].sort_values(df.columns[4], ascending=False)[:3]
    print(df_sorted)

if __name__ == "__main__":
    input_file = "annual_air_quality.csv"
    df = read_file(input_file)
    q4_max(df)
    q5_dropna_average(df)
    q6_topn(df)
    