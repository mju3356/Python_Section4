import matplotlib.pyplot

#리스트 범위(x축)
x=range(0,256)
print(x)

#리스트 범위(y축)
y=[v*v for v in x] #자동 append
#for v in x:
    #y.append(v*v)
print(y)

#차트 설정
matplotlib.pyplot.plot(x,y,'ro') #세번째 인자 선색깔(r,b),선모양(o굵게,--점선)

#차트 실행
matplotlib.pyplot.show()
