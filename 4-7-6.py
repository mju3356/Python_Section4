import FinanceDataReader
import datetime
import matplotlib.pyplot
from pandas.plotting import register_matplotlib_converters

#matplotlib Converter : 날짜(시간)관련 Warning 제거
register_matplotlib_converters()

#조회 시작 및 종료 날짜
start=datetime.datetime(2020,5,1)
end=datetime.datetime(2020,5,15)

#네이버 주식 정보 조회
gs_naver=FinanceDataReader.DataReader('035420',start,end)

#카카오 주식 정보 조회
gs_kakao=FinanceDataReader.DataReader('035720',start,end)


#출력
print(gs_naver)
print(gs_kakao)

#figure 생성
fig=matplotlib.pyplot.figure('Chart Test') #윈도우 이름 지정
#차트 사이즈 지정
fig.set_size_inches(10,6,forward=True)

#차트설정1
matplotlib.pyplot.plot(gs_naver.index,gs_naver['Close'],'b',label='Naver')
#차트설정2
matplotlib.pyplot.plot(gs_kakao.index,gs_kakao['Close'],'r',label='Kakao')

#범례위치지정
matplotlib.pyplot.legend(loc='upper left')
#차트 제목
matplotlib.pyplot.title('Naver & KaKao')
#x축 라벨
matplotlib.pyplot.xlabel('Date')
#y축 라벨
matplotlib.pyplot.ylabel('Close')

matplotlib.pyplot.show()
