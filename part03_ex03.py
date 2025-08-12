import pandas as pd
# 0:연도, 1:지역, 2:PM10, 3:PM2.5, 4:오존
def read_file(filename):
    df = pd.read_csv(filename)
    return df


def q7_pollution(df: pd.DataFrame):
    print("=========q7==========")
    df_pollution = df.copy()
    df_pollution['오염지수'] = df_pollution.iloc[:,2] * 0.6 + df_pollution.iloc[:,3] * 0.4
    df_sorted = df_pollution.groupby('연도')['오염지수'].mean().reset_index().sort_values('오염지수', ascending=False).head(1)
    print(df_sorted)

def q8_filtering(df: pd.DataFrame):
    print("=========q8==========")
    df_filtered = df[df['연도'].between(2018, 2022) & 
       (df[df.columns[2]] > 55) &
       (df[df.columns[3]] > 28)
    ]
    print(df_filtered)

def grade(x):
    if x<=30 :
        return "좋음"
    elif x <= 80:
        return "보통"
    else:
        return "나쁨"
    
def q9_grade(df: pd.DataFrame):
    print("=========q9==========")
    df["grade"] = df[df.columns[2]].apply(grade)
    df_groupped = df.groupby("grade")[df.columns[2]].count().reset_index()
    print(df_groupped)

if __name__ == "__main__":
    input_file = "annual_air_quality.csv"
    df = read_file(input_file)
    q7_pollution(df)
    q8_filtering(df)
    q9_grade(df)