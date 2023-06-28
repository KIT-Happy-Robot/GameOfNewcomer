n=int(input("数字を入力してください："))
prime_number=[]
while n!=1:
    if n%2==0:
        n//=2
        prime_number.append(2)
    elif n%3==0:
        n//=3
        prime_number.append(3)
    elif n%5==0:
        n//=5
        prime_number.append(5)
    elif n%7==0:
        n//=7
        prime_number.append(7)
    elif n%11==0:
        n//=11
        prime_number.append(11)
    elif n%13==0:
        n//=13
        prime_number.append(13)
    elif n%17==0:
        n//=17
        prime_number.append(17)
    elif n%19==0:
        n//=19
        prime_number.append(19)
    elif n%23==0:
        n//23
        prime_number.append(23)
    elif n%29==0:
        n//=29
        prime_number.append(29)
    elif n%31==0:
        n//=31
        prime_number.append(31)
    elif n%37==0:
        n//=37
        prime_number.append(37)
    elif n%41==0:
        n//=41
        prime_number.append(41)
    elif n%43==0:
        n//=43
        prime_number.append(43)
    elif n%47==0:
        n//=47
        prime_number.append(47)
    elif n% 53==0:
        n//=53
        prime_number.append(53)
    elif n%59==0:
        n//=59
        prime_number.append(59)
    elif n%61==0:
        n//=61
        prime_number.append(61)
    elif n%67==0:
        n//=67
        prime_number.append(67)
    elif n%71==0:
        n//=71
        prime_number.append(71)
    elif n%73==0:
        n//=73
        prime_number.append(73)
    elif n%79==0:
        n//=73
        prime_number.append(73)
    elif n%79==0:
        n//=79
        prime_number.append(79)
    elif n%83==0:
        n//=83
        prime_number.append(83)
    elif n%89==0:
        n//=89
        prime_number.append(89)
    elif n%97==0:
        n//=97
        prime_number.append(97)
    else:
        break
prime_number.append(n)
if min(prime_number)==1:
    prime_number.remove(1)
print(prime_number)
