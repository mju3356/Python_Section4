import urllib.request
import simplejson
import os.path

url='https://jsonplaceholder.typicode.com/comments'
Save_Name='c:/PythonApp/Section4/4-4-HomeWork.json'

if not os.path.exists(Save_Name):
    urllib.request.urlretrieve(url,Save_Name)

with open(Save_Name,'r',encoding='utf-8') as r:
    with open('c:/PythonApp/Section4/4-4-HomeWork.txt','w') as w:
        data=simplejson.load(r)
        print(data)
        for i in data:
            w.write(str(i['id'])+'  -  '+i['email']+'\n')
            print(i['id'])
