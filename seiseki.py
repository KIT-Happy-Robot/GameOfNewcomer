#理系のクラス
class Score_r:
    def __init__(self, name, senmon1, senmon2, eigo):
        self.name = name
        self.senmon1 = senmon1
        self.senmon2 = senmon2
        self.eigo = eigo
        
    def getName(self):
        return self.name
        
    def Heikin_r(self):
        return (jouhou + sugaku + eigo_r) / 3

#文系のクラス
class Score_b(Score_r):
    pass

    def Heikin_b(self):
        return (kokugo + shakai + eigo_b) / 3

#成績入力
while True:
    print("理系(r)か文系(b)をアルファベットで選択してください")
    student_part = input()
    print("注意：名前以外は全て半角での入力をお願いします！")

#成績入力（理系）
    if student_part == "r":
        print("名前を入力してください")
        name_r = input()
        print("情報の成績を入力してください")
        jouhou = int(input())
        print("数学の成績を入力してください")
        sugaku = int(input())
        print("英語の成績を入力してください")
        eigo_r = int(input())
#インスタンス作成
        s_r = Score_r(name_r, jouhou, sugaku, eigo_r)
        n_r = s_r.getName()
        h_r = s_r.Heikin_r()
        print(n_r, "さんの平均は", h_r, "です！")
        print("もう一度続けますか(y)")
        select = input()
        if select == "y":
            continue
        else:
            print("終了します")
            break
    
#成績入力（文系）                    
    elif student_part == "b":
        print("名前を入力してください")
        name_b = input()
        print("国語の成績を入力してください")
        kokugo = int(input())
        print("社会の成績を入力してください")
        shakai = int(input())
        print("英語の成績を入力してください")
        eigo_b = int(input())
#インスタンス作成
        s_b = Score_b(name_b, kokugo, shakai, eigo_b)
        n_b = s_b.getName()
        h_b = s_b.Heikin_b()
        print(n_b, "さんの平均は", h_b, "です！")
                
        print("もう一度続けますか(y)")
        select = input()
        if select == "y":
            continue
        else:
            print("終了します")
            break

