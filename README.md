Python期中報告 11124147 陳秉綜
#題目
10：針對字典D={'張三':88,'李四':90,'王五':73,'趙六':82}寫出一下操作
(1) 向字典中添加鍵值對'錢七'：90
(2) 修改'王五'對應值為93
(3) 刪除'趙六'對應的鍵值對
針對字典D={'張三':88,'李四':90,'王五':73,'趙六':82}，可以使用Python的字典方法來進行操作。

##第一題

```python
D = {'張三':88,'李四':90,'王五':73,'趙六':82}
D.update({'錢七':90})
print(D)
'''
