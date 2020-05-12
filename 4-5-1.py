import pandas

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv') #read.excel 엑셀 불러오기
#print(df)

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv',skiprows=[0,1]) #read.excel 엑셀 불러오기
#print(df)
#skiprows=행제거

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv',skiprows=[0,1],header=None) #read.excel 엑셀 불러오기
#print(df)
#header=헤더지정 None는 헤더 제거

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015]) #read.excel 엑셀 불러오기
#print(df)
#names=임의의 헤더지정

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015],index_col=[0]) #read.excel 엑셀 불러오기
#print(df)
#실데이터를 인덱스 컬럼으로 행번호 제거후 데이터를 행번호로 바꿈

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015],index_col=[0],na_values=['JAN']) #read.excel 엑셀 불러오기
#print(pandas.isnull(df))
#print(df)
#isnull true or false 로 변환,na_values 특정값으로 변환

#df=pandas.read_csv('c:/PythonApp/Section4/csv_s1.csv',skiprows=[0],header=None,names=['Month',2013,2014,2015]) #read.excel 엑셀 불러오기
#print(df.index)
#print(list(df.index))
#.index 시작 끝 간격표시
#print(df.rename(index={0:'aa',1:'bb',2:'cc'}))
#print(df.rename(index=lambda x:x*10))


#읽기
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
