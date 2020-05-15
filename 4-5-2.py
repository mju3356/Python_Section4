import pandas
df2=pandas.read_csv("c:/PythonApp/Section4/csv_s2.csv",sep=';',skiprows=[0],header=None,names=['Name','Test1','Test2','Test3','Final','Grade'])
#print(df)
#sep= 구분자 지정

#컬럼 수정
#df2['Grade']=df2['Grade'].str.replace('C','A++')
#print(df2)
#str.replace 컬럼 수정

#평균 컬럼 추가
df2['Avg']=df2[['Test1','Test2','Test3','Final']].mean(axis=1)


#합계 컬럼 추가
df2['Sum']=df2[['Test1','Test2','Test3','Final']].sum(axis=1)
print(df2)


df2.to_csv('c:/PythonApp/Section4/result_csv.csv',index=False)

#파일 저장,index=False는 행번호 제거
