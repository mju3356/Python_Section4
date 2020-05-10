#딕셔너리 자료형(Key,Value) -> (순서x,중복x,수정o,삭제o)

#선언
a={'name':'kim','phone':'010-1234-5678','birth':10626}
b={0,'Hello World'}
c={'arr':[0,1,2,3]}
print(type(a),a)

#출력
print('a - ',a['name'])
print('a - ',a.get('phone')) #get은 없으면 오류가 아니라 none if문 활용
print('c - ',c.get('arr'))

#딕셔너리 추가
a['address']='JeonBuk'
print('a - ',a)
a['rank']=[1,2,3]
print('a - ',a)

print('a - ',list(a.keys()))
print('a - ',a.keys())

print('a - ',list(a.values()))
print('a - ',a.values())

print('a - ',a.items())
print('a - ',type(list(a.items())[0]))

print('a - ','name' in a)
print('a - ','city' in a)#안에 있는지 검색(키값만 검색)
