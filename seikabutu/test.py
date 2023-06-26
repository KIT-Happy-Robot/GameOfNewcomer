import time
import random

print("今からタイピングゲームを始めます")
print("文字が出力されるので同じ文字を入力してください")
print("問題は全部で７問です")
y=input("準備ができたらyを押してください")
time_start=time.time()
mozi=['egg','python','program','university','terminal','student','accident']
i=0
while i<=6:
    print(mozi[i])
    ans=input()
    if mozi[i]!=ans:
        while mozi[i]!=ans:
            print("もう一度打ち直し")
            ans=input()
    i+=1
time_end=time.time()-time_start
print("これで終了です")
print("{:.2f}秒かかりました".format(time_end))