import pandas as pd

def read_file(filename):
    df = pd.read_csv(filename)
    return df

def q3_check_na(df: pd.DataFrame):
    print("=========q3==========")
    q3 = df[df.iloc[:, 3].isna()]
    print(q3)

def q2_process_data(df: pd.DataFrame):
    print("=========q2==========")
    df_filtered = df[(df.iloc[:,3] >= 30) & (df['연도'] == 2020)]
    print(df_filtered)
    
def q1_average(df: pd.DataFrame):
    print("=========q1==========")
    df_average = df.groupby('연도')[df.columns[2]].mean().reset_index().sort_values("연도", ascending=False)
    print(df_average)

if __name__ == "__main__":
    input_file = "annual_air_quality.csv"
    df = read_file(input_file)
    q3_check_na(df)
    q2_process_data(df)
    q1_average(df)
    