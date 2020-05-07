import pickle #객체 텍스트 직렬화,역질렬화

#파일이름과 데이터
B_Filename='c:/PythonApp/Section4/test.bin'
T_Filename='c:/PythonApp/Section4/test.text'

data1=77
data2='Hello World'
data3=['car','apple','house']

#바이너리쓰기
with open(B_Filename,'wb') as f:
    pickle.dump(data1,f) #dumps(문자열 직렬화)
    pickle.dump(data2,f)
    pickle.dump(data3,f)

#텍스트쓰기
with open(T_Filename,'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(data2)
    f.write('\n')
    f.writelines('\n'.join(data3))
    #writelines 배열 문자

#바이너리 읽기
with open(B_Filename,'rb') as f:
    b=pickle.load(f) #loads 문자열 역질렬화
    print(type(b),'Binary Read1 |',b)
    b=pickle.load(f)
    print(type(b),'Binary Read2 |',b)
    b=pickle.load(f)
    print(type(b),'Binary Read3 |',b)

#텍스트읽기

with open(T_Filename,'rt') as f:
    for i,line in enumerate(f,1):
        print(type(line),'Text Read' + str(i) + ' | ', line,end="")
