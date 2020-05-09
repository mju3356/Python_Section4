import sys,io
import urllib.request
from bs4 import BeautifulSoup
import os.path #경로검색

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

#다운로드 url
url='http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
Save_Name="c:/PythonApp/Section4/Weather_Info.xml"

if not os.path.exists(Save_Name): #저장되어있는지 확인
    urllib.request.urlretrieve(url,Save_Name) #중복다운로드를 방지하여 과부하 방지

#BeautifulSoup 파싱
xml=open(Save_Name,'r',encoding='utf-8')
soup=BeautifulSoup(xml,'html.parser')

#지역확인
Info={}
for location in soup.find_all('location'):
    loc=location.find('city').string
    #print(loc)
    Weather=location.find_all('tmn')
    #print(Weather)
    if not (loc in Info): #중복검색
        Info[loc]=[]
    for tmn in Weather:
        Info[loc].append(tmn.string)
#print(Info)


# 각 지역별 날씨 텍스트 쓰기
# sorted 오름차순 정렬
with open('c:/PythonApp/Section4/Weather_Info.txt','w',encoding='utf-8') as f:
    for loc in sorted(Info.keys()):
        print('+',loc)
        f.write(str(loc)+'\n')
        for n in Info[loc]:
            print('-',n)
            f.write('\t'+str(n)+'\n')
