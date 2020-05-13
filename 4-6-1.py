import pandas

#기본 읽기1
#df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',sheet_name=0)
#print(df)
#print(df.head()) 상위 5개
#print(df.tail()) 하위 5개

#행,푸터(footer)(테일)스킵
#df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',skiprows=[0],skipfooter=10)
#print(df)

#헤더 정의(1)
#df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',header=1) #해당열의 값을 올러씀
#print(df)
#print(list(df))
#print(list(df.columns.values))

#헤더정의(2)
#df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',skiprows=[0],header=None,names=["State",2003,2004,2005])
#print(df)

#특정 값 치환
#df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',header=0,na_values='...',converters={'2003': lambda w: w if w > 60000 else None}) #해당열의 값을 올러씀
#print(df)
#print(pandas.isnull(df))

#실습 정리 및 인덱스 재정의
df=pandas.read_excel('c:/PythonApp/Section4/excel_s1.xlsx',header=0) #해당열의 값을 올러씀
print(df)
print(df.rename(index=lambda x:x+10))
print(df.rename(index=lambda x:x+10).index)
