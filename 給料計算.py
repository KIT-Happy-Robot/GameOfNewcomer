import math

s = float(input("開始時刻XX\n"))
e = float(input("終了時刻XX\n"))
h = float()
w = float()
hw1 = 1000
hw2 = 1250
l1 = float()
l2 = float()
lr = 7/6
sr =1/6

h = e - s
lr = round(lr, 3)
sr = round(sr, 3)

if h >= 6:
    h -= lr
else:
    h -= sr

if s <= 22 and e >= 29:
    l1 = 22 - s
    h -= l1
    l2 = e - 29
    h -= l2
    w = l1 * hw1 + h * hw2 + l2 * hw1
elif s >= 22 and e <= 29:
    l2 = e - 29
    h -= l2
    w = h * hw2 + l2 * hw1
elif s <= 22 and e >= 29:
    l1 = s - 22
    h -= l1
    w = h * hw2 + l1 * hw1
else:
    w = h * hw1

w = round(w)
print(w)