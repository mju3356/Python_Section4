import sys,io
import urllib.request
from bs4 import BeautifulSoup
import os.path #경로검색

sys.stdout=io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

URL='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=146'
Save_Name='c:/PythonApp/Section4/4-2-HomeWork.xml'

if not os.path.exists(Save_Name):
    urllib.request.urlretrieve(URL,Save_Name)

XML=open(Save_Name,'r',encoding='utf-8')
Soup=BeautifulSoup(XML,'html.parser')

data=Soup.find_all('location')
for a in data:
    if a.find('city').string=='익산':
        with open('c:/PythonApp/Section4/IkSan_Weather.txt','w',encoding='utf-8') as f:
            for index,i in enumerate(a.find_all('tmef')):
                f.write('날짜:'+str(i.string)+'\n')
                f.write('날씨:'+str(a.find_all('wf')[index].string)+'\n')
                f.write('최저기온:'+str(a.find_all('tmn')[index].string)+'\n')
                f.write('최고기온:'+str(a.find_all('tmx')[index].string)+'\n')
                f.write('\n')
