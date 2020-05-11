import urllib.request
import simplejson
import os.path

#url
url='https://api.github.com/repositories'

#경로,파일명
savename='c:/PythonApp/Section4/repo.json'

if not os.path.exists(savename):
    urllib.request.urlretrieve(url,savename)
#중복검사

items=simplejson.load(open(savename,'r',encoding='utf-8'))


#출력
for item in items:
    print(item['full_name']+'  -  '+item['owner']['url'])

#indent를 사용할거면 dumps 아니면 간편한 dump load,loads는 잘모르겠음
