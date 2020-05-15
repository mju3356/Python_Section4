import FinanceDataReader
import datetime
import matplotlib.pyplot
from pandas.plotting import register_matplotlib_converters
import pandas

#matplotlib Converter : 날짜(시간)관련 Warning 제거
register_matplotlib_converters()

start_date=datetime.datetime(2020,4,1)
end_date=datetime.datetime(2020,4,15)

gs_osung=FinanceDataReader.DataReader('052420',start_date,end_date)
gs_zeus=FinanceDataReader.DataReader('079370',start_date,end_date)


gs_osung.to_excel('c:/PythonApp/Section4/Osunggam.xlsx')
gs_zeus.to_excel('c:/PythonApp/Section4/Zeus.xlsx')

fig=matplotlib.pyplot.figure('주식 차트')
fig.set_size_inches(10,6,forward=True)

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)
'''
ax1.title('Osung & Zeus (OPEN) ')
ax2.title('Osung & Zeus (HIGH) ')
ax3.title('Osung & Zeus (LOW) ')
ax4.title('Osung & Zeus (CLOSE) ')
ax1.xlabel('DATE')
ax2.xlabel('DATE')
ax3.xlabel('DATE')
ax4.xlabel('DATE')
ax1.ylabel('VALUE')
ax2.ylabel('VALUE')
ax3.ylabel('VALUE')
ax4.ylabel('VALUE')
'''


ax1.plot(gs_osung.index,gs_osung['Open'],'r',label="Osung")
ax1.plot(gs_zeus.index,gs_zeus['Open'],'b',label="Zeus")
ax2.plot(gs_osung.index,gs_osung['High'],'r',label="Osung")
ax2.plot(gs_zeus.index,gs_zeus['High'],'b',label="Zeus")
ax3.plot(gs_osung.index,gs_osung['Low'],'r',label="Osung")
ax3.plot(gs_zeus.index,gs_zeus['Low'],'b',label="Zeus")
ax4.plot(gs_osung.index,gs_osung['Close'],'r',label="Osung")
ax4.plot(gs_zeus.index,gs_zeus['Close'],'b',label="Zeus")

matplotlib.pyplot.show()
