D = {'張三':88,'李四':90,'王五':73,'趙六':82}
D.update({'錢七':90})
print(D)
D['王五'] = 93
print(D)
D.pop('趙六')
print(D)