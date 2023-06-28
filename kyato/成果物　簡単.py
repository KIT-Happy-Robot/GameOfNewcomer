import random
import time
from time import sleep

n = 0
success = 0
miss = 0
Mole_appear_time = random.randint(1,10)
hit_possible_time = random.random()
while True:
    Mole_appear_time = random.randint(1,10)
    print("モグラが出てきたら殴れ")
    sleep(Mole_appear_time)
    print("ひょこ")
    capture_start_time = time.time()
    capture = input("今だ!![enter]")
    capture_end_time = time.time()
    diff_capture_time = capture_end_time - capture_start_time
    n +=1
    
    if diff_capture_time < hit_possible_time:
        print("ナイス")
        success +=1
    else:
        print("逃げられた…")
        miss +=1
    if n == 5:
        break
print("結果は…")
sleep(Mole_appear_time)
if success >= 5:
    print("パーフェクト！！")
      
elif success >= 3:
    print("惜しい！！")
      
else:
    print("ドンマイ!!")