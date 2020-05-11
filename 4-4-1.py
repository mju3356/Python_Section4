import simplejson

#Dict(Json)선언
data={}
data['people']=[]
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})

data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})

data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Incheon'
})


#Dict(Json) -> str

e=simplejson.dumps(data,indent=1) #indent=들여쓰기 조절
#print(type(e),e)

#str -> Dict(Json)

d=simplejson.loads(e)
#print(type(d),d)

with open('c:/PythonApp/Section4/menber.json','w') as outfile:
    outfile.write(e)

with open('c:/PythonApp/Section4/menber.json','r') as infile:
    r=simplejson.loads(infile.read()) #read를 붙여야 str형태
    print('==============')
    print(type(r))
    print(r)
    for p in r['people']:
        print('Name: '+p['name'])
        print('Website: '+p['website'])
        print('From: '+p['from'])
        print('')
