import random

def SYOUHAI(WATASI, KIKAI):
    if WATASI == KIKAI:
        return "引き分け"
    elif (WATASI == "グー" and KIKAI == "チョキ")or \
         (WATASI == "チョキ" and KIKAI == "パー") or \
         (WATASI == "パー" and KIKAI == "グー"):
        return "お前の価値"
    else:
        return "機械のの勝ち"

choices = ["グー", "チョキ", "パー"]

WATASI = input("グー、チョキ、パーのいずれかを入力してください: ")
KIKAI = random.choice(choices)

print("ユーザーの選択:", WATASI)
print("コンピュータの選択:", KIKAI)

KATI = SYOUHAI(WATASI, KIKAI)
print("結果:", KATI)
