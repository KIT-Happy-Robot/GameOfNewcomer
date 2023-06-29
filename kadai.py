
import random
a=random.randrange(1,6)
b=random.randrange(1,6)
print(a,b)
if a==1 and b==1:
  print('ピンゾロの')
if a==1 and b==2 or a==2 and b==1:
  print('イチニの')
if a==1 and b==3 or a==3 and b==1:
  print('サンミチの')
if a==1 and b==4 or a==4 and b==1:
  print('ヨイチの')
if a==1 and b==5 or a==5 and b==1:
  print('グイチの')
if a==1 and b==6 or a==6 and b==1:
  print('イチロクの')
if a==2 and b==2:
  print('二ゾロの')
if a==2 and b==3 or a==3 and b==2:
  print('サニの')
if a==2 and b==4 or a==4 and b==2:
  print('シニの')
if a==2 and b==5 or a==5 and b==2:
  print('グニの')
if a==6 and b==6 or a==6 and b==2:
  print('ニロクの')
if a==3 and b==3:
   print('サンゾロの')
if a==3 and b==4 or a==4 and b==3:
    print('シソウの')
if a==3 and b==5 or a==5 and b==3:
   print('グサンの')
if a==3 and b==6 or a==6 and b==3:
  print('サブロクの')
if a==4 and b==4:
  print('シゾロの')
if a==4 and b==5 or a==5 and b==4:
  print('グシの')
if a==4 and b==6 or a==6 and b==4:
  print('シロクの')
if a==5 and b==5:
   print('ゴゾロの')
if a==5 and b==6 or a==6 and b==5:
  print('ゴロクの')
if a==6 and b==6:
  print('ロクゾロの')
c=a+b
if c % 2==0:
  print('丁')
else:
  print('半')
