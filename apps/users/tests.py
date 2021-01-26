import hashlib

hash = hashlib.sha256()
hash.update('debug5.com'.encode('utf-8'))
print(hash.hexdigest())

m = hashlib.md5()
m.update('debug5.com'.encode('utf-8'))
print(m.hexdigest())

m = hashlib.md5('debug5'.encode('utf-8'))
m.update('.com'.encode('utf-8'))
print(m.hexdigest())

'''
passwds = ['123456','4564','3413','413','413','debug5.com',]
s = '49f918671be658f2a8517d0a6662eef0'

def pipei(list1,str1):

      for i in list1:
            m = hashlib.md5()
            m.update(i.encode('utf-8'))
            print(m.hexdigest())
            if str1 == m.hexdigest():
                  return i
      return '不存在'

print(pipei(passwds,s))
'''




