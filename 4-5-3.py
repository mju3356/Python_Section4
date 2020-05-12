import pandas
import numpy


#랜덤으로 DataFrame 생성
df=pandas.DataFrame(numpy.random.randint(0,100,size=(100,4)),columns=list('ABCD'))
df=pandas.DataFrame(numpy.random.randn(100,4),columns=['One','Two','Three','Four'])
print(df)

df.to_csv('c:/PythonApp/Section4/result_csv2.csv',index=False,header=False)
