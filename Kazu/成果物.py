import random
count = 0
total = 0
Matoate = [1000, 500, 100, 10, 0]
while count < 4:
    i = random.choice(Matoate)
    count += 1
    total += i
if total >= 3000:
    gift = 'ディズニー年間パスポート'
elif total >= 2000:
    gift = 'Nintendo-Switch'
elif total >= 1500:
    gift = 'Amazonギフト券1000円'
else:
    gift = 'うまい棒10本＆カップラーメン１個'
print(f'おめでとう！{gift}をプレゼント！')