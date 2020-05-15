import pandas_datareader.data
import datetime

#조회 시작날짜
start=datetime.datetime(2020,5,15)
end=datetime.datetime(2020,5,30)

#Google 정보 호출
GS=pandas_datareader.DataReader('KRX: 035720','google',start,end)
print(GS)
