print("数当てゲーム")
import random
a = str(random.randint(0,9))
while True:
    b = str(random.randint(0,9))
    if a != b:
        break
    else:
        continue
while True:
    c = str(random.randint(0,9))
    if a != c and b != c:
        break
    else:
        continue
while True:
    d = str(random.randint(0,9))
    if a != d and b != d and c != d:
        break
    else:
        continue

NPC = [a,b,c,d]
k = "".join(NPC)
print ("私は４つの数字を持っています。その数を１０回以内に当ててみてね。")
n = 10

while n >= 1:
    print(n)
    n -= 1
    m = 0
    nm = 0
    ans = str(input("数値を入力"))
    if ans == k:
        print("正解！素晴らしい！")
        break
    else:
        if ans[0] in [a,b,c,d]:
            m += 1
            if a == ans[0]:
                nm += 1
        if ans[1] in [a,b,c,d]:
            m += 1
            if b == ans[1]:
                nm += 1
        if ans[2] in [a,b,c,d]:
            m += 1
            if c == ans[2]:
                nm += 1
        if ans[3] in [a,b,c,d]:
            m += 1
            if d == ans[3]:
                nm += 1
                
        if n != 0:
            print("含まれている数",m,"個で、その中でも位置もあっているのは",nm,"個です。")
        else:
            if m == 4:
                print("頑張れ！")
            elif nm >= 2:
                print("おしい！次はいける")
                
            print("正解は",k,"でした。")
        continue
