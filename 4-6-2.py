import pandas

df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',header=0) #해당열의 값을 올러씀
#print(df)

#컬럼 값 수정
#df['State']=df['State'].str.replace(' ','|')#010-3333-7777
#print(df)
#정규표현식 사용시 편함

#평균 컬럼 추가
df["Avg"]=df[['2003','2004','2005']].mean(axis=1).round(2) #1은 열 방향 0은 행방향 #round 반올림
#print(df)

#합계 컬럼 추가
df["Sum"]=df[['2003','2004','2005']].sum(axis=1)
#print(df)

#최대값 출력
#print(df[['2003','2004','2005']].max(axis=0))

#최소값 출력
#print(df[['2003','2004','2005']].min(axis=0))

#상세 정보 출력
#print(df.describe())


df.to_excel('c:/PythonApp/Section4/result_s1.xlsx')
