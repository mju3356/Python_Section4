import pandas

df=pandas.read_csv('c:/PythonApp/Section4/FL_insurance_sample.csv',skiprows=[0],header=None)
df=df.rename(index=lambda x:x*10)
df.to_csv('c:/PythonApp/Section4/4-5-HomeWork.csv',index=None)
