import matplotlib.pyplot

#figure 객체 설정
fig=matplotlib.pyplot.figure()

#서브 블롯 생성(2행 1열)
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

#x축
x=range(0,100)

#y축
y=[v*v for v in x]

#y축2
z=[v*v*2 for v in x]

#라인차트(1행1열)
ax1.plot(x,y,'b--',z,'ro') #2개 입력시 차트 2개 중복가능

#Bar차트(2행1열)
ax2.bar(x,z)

matplotlib.pyplot.show()
