##　エリア３つ
##アイテム4つまで　超えた場合は交換選択
##　@敵　￥ショップ　？探索場所　！イベント　　＃宝箱　＊探索済み　＿無し
##攻撃はアイテム基本　なくなった時は低めのダメージ
import random

class Color:
    ##色 
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    
class state:
    ##プレイヤー
    gold = 50
    hp = 100
    ##初期通５
    Itemlist = [
        [1,"初級の杖",5],
        [2,"なし",0],
        [3,"なし",0],
        [4,"なし",0]
    ]
    ##敵
    enmdata = [
        ["name","hp","gold","Item","num","先制攻撃"],
        ["雑魚１",25,20,"回復ポーション小",2,0],
        ["雑魚2",30,25,"中級の杖",2,0],
        ["雑魚3",27,25,"投げナイフ",1,2],
        ["中ボス１",45,50,"上級の杖",2,5],
        ["中ボス２",60,100,"回復ポーション大",2,6],
        ["ボス",80,500,"上級の杖",2,0]
    ]
    ##ショップ
    shoplist = [
        ["番号","名前","個数","値段"],
        [1,"中級の杖",4,200],
        [2,"回復ポーション中",4,250],
        [3,"上級の杖",3,300],
        [4,"回復ポーション大",3,350]
    ]   

    ##イベント
    data_floor1 = ['＠','？','？','！']
    data_floor2 = ['＠','￥','？','＃','！']    
    data_floor3 = ['＠','＠','？','？','？','！','＃']
    ##シャッフル
    random.shuffle(data_floor1)
    random.shuffle(data_floor2)    
    random.shuffle(data_floor3)
    ##フロアランダム
    point1 = [data_floor1[0],data_floor1[1],data_floor1[2],data_floor1[3]]
    point2 = [data_floor2[0],data_floor2[1],data_floor2[2],data_floor2[3],data_floor2[4]]
    point3 = [data_floor3[0],data_floor3[1],data_floor3[2],data_floor3[3],data_floor3[4],data_floor3[5],data_floor3[6]]
    ##フロア２
    floor2 = [
        ['＿',point2[0],'＿','＿'],
        ['＿','＿','＿','＿'],
        [point2[1],'＿',point2[3],'＿'],
        ['＿','＿',point2[2],point2[4]]
    ]     
    ##３フロア目
    floor3 = [
        ['＿',point3[0],'＿',point3[4],'＿'],
        ['＿','＿','＿','＿',point3[5]],
        [point3[1],'＿','＿','＿','＿'],
        ['＿',point3[2],'＿','＿',point3[6]],
        ['＿','＿',point3[3],'＿','＿']
    ]
    ##フロア１
    floor1 = [
        [point1[0],'＿','＿','＿'],
        ['＿',point1[1],'＿','＿'],
        ['＿','＿','＿',point1[2]],
        ['＿',point1[3],'＿','＿']
    ]

def enem(flg):
##1フロアボス 2フロアボス 3フロアボス 4雑魚
    if flg == 1:
        ##中ボス１
        enmr = 4
        enmname = state.enmdata[4][0]
        enmhp = state.enmdata[4][1]
        enmflg = state.enmdata[4][5]
    elif flg == 2:
        ##中ボス２
        enmr = 5
        enmname = state.enmdata[5][0]
        enmhp = state.enmdata[5][1]
        enmflg = state.enmdata[5][5]
    elif flg == 3:
        ##ボス
        enmr = 6
        enmname = state.enmdata[6][0]
        enmhp = state.enmdata[6][1]
        enmflg = state.enmdata[6][5]
    else:
        ##雑魚
        enmr = random.randint(1,3)
        enmname = state.enmdata[enmr][0]
        enmhp = state.enmdata[enmr][1]
        enmflg = state.enmdata[enmr][5]
    print(f'{Color.UNDERLINE}{Color.CYAN}{enmname}が現れた{Color.END}')
    
    if enmflg > 0:
        ##先制攻撃判定
        print(f'{Color.PURPLE}{enmname}の先制攻撃{Color.END}')
        print(f'{Color.RED}{enmflg}ダメージを受けた{Color.END}')
        state.hp -= enmflg
    while (enmhp > 0) and (state.hp > 0):
        ##攻撃選択
        selc = ""
        itemselc = ""
        tflug = 0
        print(f'あなたのhp:{state.hp}')
        print(f'{Color.GREEN}コマンドを選択してください{Color.END}')
        ##入力　例外判定
        while type(selc) != int: 
            try:
                selc = int(input(Color.UNDERLINE + Color.BLUE + '1 攻撃,2 アイテム' + Color.END))
            except ValueError:
                print("エラーです　数字を入力してください")
            print()
        if selc == 1:
            ##アイテム無し攻撃
            dmg = random.randint(4,7)
            print(f'あなたの攻撃 敵hpが-{dmg}')
            tflug = 1
        elif selc == 2:
            ##アイテム選択
            print(state.Itemlist[0])
            print(state.Itemlist[1])
            print(state.Itemlist[2])
            print(state.Itemlist[3])
            ##入力　例外判定
            while type(itemselc) != int:
                try:
                    itemselc = int(input(Color.UNDERLINE + Color.BLUE + '使用するアイテムを選択してください　戻る場合は5を入力してください' + Color.END))
                except ValueError:
                    print(f"{Color.RED}エラーです　数字を入力してください{Color.END}")
            if itemselc == 5:
                print("前の入力に戻ります")
            elif itemselc > 5 or itemselc < 1:
                print(f"{Color.RED}エラーです　有効な数字を入力してください{Color.END}")
            elif state.Itemlist[itemselc - 1][2] == 0:
                print("持っていません")
            elif 1 <= itemselc and itemselc <= 4:
                ##アイテム使用
                enmhp = useItm(itemselc,enmhp)
                tflug = 1
            else:
                print(f"{Color.RED}無効な入力ですもう一度入力してください{Color.END}")
        if enmhp <= 0:
            ##勝利判定
            print(f'{Color.YELLOW}{enmname}に勝利した{Color.END}')
            print(f'{state.enmdata[enmr][3]}を{state.enmdata[enmr][4]}入手した')
            print(f'{Color.YELLOW}{state.enmdata[enmr][2]}gold手に入れた{Color.END}')
            state.gold += state.enmdata[enmr][2]
            Itm(state.enmdata[enmr][3],state.enmdata[enmr][4])
        elif tflug == 1:
            print()
            ##敵攻撃
            if enmr == 4 or enmr == 5:
                dmg = random.randint(10,16)
            elif enmr == 6:
                dmg = random.randint(18,35)
            else:
                dmg = random.randint(5,10)
            print(f"{Color.PURPLE}{enmname}の攻撃{Color.END}")
            print(f'{Color.RED}{dmg}ダメージを受けた{Color.END}')
            state.hp -= dmg
        if state.hp <= 0:
            print("敗北した")
            break

def useItm(selc,enhp):
    ##アイテム個数を減らす　0になったら初期化
    itemname = state.Itemlist[selc - 1][1]
    state.Itemlist[selc - 1][2] -= 1
    print(f'{itemname}を使用しました')
    if state.Itemlist[selc - 1][2] == 0:
        state.Itemlist[selc - 1][1] = 'なし'
    ##アイテム効果
    if itemname == "初級の杖":
        ##テスト用
        ##mov = random.randint(50,50)
        ##通常
        mov = random.randint(9,12)
        print(f'{Color.GREEN}敵hpに{mov}ダメージ{Color.END}')
        return enhp - mov
    elif itemname == "中級の杖":
        mov = random.randint(18,23)
        print(f'{Color.GREEN}敵hpに{mov}ダメージ{Color.END}')
        return enhp - mov
    elif itemname == "上級の杖":
        mov = random.randint(35,40)
        print(f'{Color.GREEN}敵hpに{mov}ダメージ{Color.END}')
        return enhp - mov
    elif itemname == "投げナイフ":
        mov = random.randint(35,60)
        print(f'{Color.GREEN}敵hpに{mov}ダメージ{Color.END}')
        return enhp - mov
    elif itemname == "回復ポーション小":
        mov = 15
        print(f'{Color.GREEN}体力が{mov}回復した{Color.END}')
        state.hp += mov
    elif itemname == "回復ポーション中":
        mov = 30
        print(f'{Color.GREEN}体力が{mov}回復した{Color.END}')
        state.hp += mov
    else:
        mov = 50
        print(f'{Color.GREEN}体力が{mov}回復した{Color.END}')
        state.hp += mov
    if state.hp > 100:
        state.hp = 100
    return enhp
        
def Itm(Itemname,num):
    print(f'{Color.UNDERLINE}{Itemname}を{num}個見つけた{Color.END}')
    change = ""
    if not(state.Itemlist[0][2] == 0 or state.Itemlist[1][2] == 0 or state.Itemlist[2][2] == 0 or state.Itemlist[3][2] == 0):
        change = printItm()
        if change == 5:
            print(f'{Color.RED}{Itemname}を{num}個捨てました。{Color.END}')
        elif change >= 1 and change <= 4:
            ##アイテム交換　名前　個数の更新
            print(f'{Color.GREEN}{state.Itemlist[change - 1][1]}を{Itemname}に交換しました{Color.END}')
            state.Itemlist[change - 1][1] = Itemname
            state.Itemlist[change - 1][2] = num
    else:
        ##空きがあるとき　最初に見つけたなしの部分を更新
        print(f'{Color.GREEN}{Itemname}を追加しました{Color.END}')
        i = 0
        while i < 5:
            now = state.Itemlist[i][1]
            if now == "なし":    
                state.Itemlist[i][1] = Itemname
                state.Itemlist[i][2] = num
                break
            i += 1
    print()

def printItm():
    change = ""
    print("アイテムを交換しますか？")
    print(state.Itemlist[0])
    print(state.Itemlist[1])
    print(state.Itemlist[2])
    print(state.Itemlist[3])
    ##入力　例外判定
    while type(change) != int:
        while type(change) != int:
            try:
                change = int(input(Color.UNDERLINE + Color.BLUE + "交換する番号を入力してください　交換しない場合は5を入力してください" + Color.END))
            except ValueError:
                print(f"{Color.RED}エラーです　数字を入力してください{Color.END}")
        if change > 5 or change < 1:
            print(f"{Color.RED}エラーです　有効な数字を入力してください{Color.END}")
            change = ""
    return change

def treg(flg):
    print(f"{Color.UNDERLINE}あなたは宝箱をあけた{Color.END}")
    if flg == 1:
        Itm("上級の杖",4)
    ##探索宝箱
    rand1 = random.randint(0,1)
    if rand1 == 0:
        Itm("回復ポーション中",3)
    else:
        Itm("中級の杖",3)

def sear():
    ##探索　ランダム６つ
    print(f"{Color.UNDERLINE}あなたは探索を始めた{Color.END}")
    rand_se = random.randint(0,5)
    if rand_se == 0:
        print("木箱を見つけた")
        print("あけてみると、アイテムが入っていた")
        Itm("上級の杖",2)
    elif rand_se == 1:
        print("古いバックを見つけた")
        print("中には少量のお金とアイテムが入っていた")
        Itm("回復ポーション中",2)
        state.gold += 25
    elif rand_se == 2:
        print("隠された物置を見つけた")
        print("中にはアイテムが入っていた")
        rend_se2 = random.randint(0,1)
        if rend_se2 == 0:
            Itm("回復ポーション大",2)
        else:
            Itm("投げナイフ",1)
    elif rand_se == 3:
        print("金貨の入った袋を見つけた")
        print(f"{Color.YELLOW}お金を100gold見つけた{Color.END}")
        state.gold += 100
    elif rand_se == 4:
        print("宝箱を見つけた")
        treg(0)
    else:
        print(f"{Color.PURPLE}敵が現れた{Color.END}")
        enem(4)
    print()

def eve():
    ##１と２以外のときの例外処理を入れる
    ##イベント処理３種類
    fin = 0;
    ehehe = ""
    rand_ev = random.randint(0,2)
    if rand_ev == 0:
        print("大きな木がある。揺らしてみますか？")
        ehehe = printeve()
        if ehehe == 1:
            state.gold += 100 
            print(f"{Color.YELLOW}木からお金が降ってきた　100goldを入手した{Color.END}")
    elif rand_ev == 1:
        print("小さな箱がある。あけてみますか？")
        ehehe = printeve()
        if ehehe == 1:
            state.hp -= 5
            print(f"{Color.RED}罠だった　５ダメージを受けた{Color.RED}")
    elif rand_ev == 2:
        print("大きな箱がある。あけてみますか？")
        while type(ehehe) != int:
            ehehe = printeve()
        if ehehe == 1:
            rand_im = random.randint(0,1)
            if rand_im == 0:
                Itm("中級の杖",3)
            else:
                Itm("回復ポーション小",3)
    if ehehe == 2:
        print("あなたはそのまま立ち去った")

def printeve():
    ehehe = ""
    while type(ehehe) != int:
        while type(ehehe) != int:
            try:
                ehehe = int(input(Color.UNDERLINE + Color.BLUE + "1はい 2いいえ" + Color.END))
            except ValueError:
                print(f"{Color.RED}エラーです　数字を入力してください{Color.END}")
        if ehehe == "" or (ehehe > 2 or ehehe < 1):
            print(f"{Color.RED}エラーです　有効な数字を入力してください{Color.END}")
            ehehe = ""
    return ehehe

def shop():
    ##ショップ
    sel = printshop()
    ##５（退出）のとき以外にwhileに入る
    while sel != 5:
        if sel < 1 or sel > 4:
            print(f"{Color.RED}無効な数字です{Color.RED}\n")
        elif state.shoplist[sel][1] == "売り切れ":
            print(f"{Color.RED}購入済みです{Color.END}")
        else:
            ##購入できない状態のときの処理
            if state.shoplist[sel][3] > state.gold:
                print(f"{Color.RED}所持金額が足りません{Color.RED}")
            elif sel <= 4 and sel >= 1:
                Itm(state.shoplist[sel][1],state.shoplist[sel][2])
                state.shoplist[sel][1] = "売り切れ"
        sel = printshop()
        
    print("あなたはショップから立ち去った")
    print()

def printshop():
    sel = ""
    print(f"{Color.UNDERLINE}ショップを見つけた{Color.END}")
    print(state.shoplist[0])
    print(state.shoplist[1])
    print(state.shoplist[2])
    print(state.shoplist[3])
    print(state.shoplist[4])
        
    print("購入したいアイテムの番号を入力してください　退出は５を入力")
    while type(sel) != int:
        try:
            sel = int(input(Color.UNDERLINE + Color.BLUE + "番号を入力" + Color.END))
        except ValueError:
            print(f"{Color.RED}エラーです　数字を入力してください{Color.END}")
    return sel

def mainprint():
    ##場所選択時のメッセージ　入力
    print("\n@敵　￥ショップ　？探索場所　！イベント　＃宝箱　＿無し")
    print("全３フロア、全ての＠(敵)を撃破したら次のフロアに進みます")
    print(f'{Color.GREEN}HP：{state.hp}  お金：{state.gold}{Color.END}')
    key = input(Color.UNDERLINE + Color.BLUE + "探索する場所の記号を入力してください　" + Color.END)
    print("\n入力された記号：" + key)
    return key

def game(gameflg):
    key = ""
    ##1
    if gameflg == 1:
        while state.point1.count("＠") > 0:
            print(Color.CYAN+"-１フロア目マップ-"+ Color.END)
            print(state.floor1[0])
            print(state.floor1[1])
            print(state.floor1[2])
            print(state.floor1[3])
            key = mainprint()
            
            ##フロア１探索　＠　！　？
            if key in state.point1:
                idx = state.point1.index(key)
                if key == "＿" :
                    print(Color.GREEN + "特に何も見つからなかった\n" + Color.END)
                elif key == "＠" :
                    enem(1)
                elif key == "！":
                    eve()
                elif key == "？":
                    sear()
                state.point1[idx] = "＊"
            else:
                if key == "！" or key == "？":
                    print(f'{Color.RED}{key}の残り探索回数は０です{Color.END}')
                else:
                    print(Color.RED+ "無効な記号です"+ Color.END)
                    print(Color.RED+ "もう一度入力してください（記号は大文字です）"+ Color.END)
        ##2
    elif gameflg == 2:
        while state.point2.count("＠") > 0:
            print(f'{Color.CYAN}-2フロア目マップ-{Color.END}')
            print(state.floor2[0])
            print(state.floor2[1])
            print(state.floor2[2])
            print(state.floor2[3])
            key = mainprint()
            
            ##フロア２探索　＠　！　？　＃　￥
            if key in state.point2:
                idx = state.point2.index(key)
                if key == "＿" :
                    print(Color.GREEN + "特に何も見つからなかった\n" + Color.END)
                elif key == "＠" :
                    enem(2)
                elif key == "！":
                    eve()
                elif key == "￥":
                    shop()
                elif key == "＃":
                    treg(0)
                elif key == "？":
                    sear()
                else:
                    if key == "！" or key == "？" or key == "＃":
                        print(f'{Color.RED}{key}の残り探索回数は０です{Color.END}')
                state.point2[idx] = "＊"
            else:
                print(Color.RED+ "無効な記号か存在しません"+ Color.END)
                print(Color.RED+ "もう一度入力してください（記号は大文字です）"+ Color.END)
        ##3
    else:
        count = 0
        while state.point3.count("＠") > 0:
            if state.hp <= 0:
                return 1
            print(Color.CYAN+"-3フロア目マップ-"+ Color.END)
            print(state.floor3[0])
            print(state.floor3[1])
            print(state.floor3[2])
            print(state.floor3[3])
            print(state.floor3[4])
            key = mainprint()
             
                ##フロア３探索　＠*2　！　？　＃
            if key in state.point3:
                idx = state.point3.index(key)
                if key == "＿" :
                    print(Color.GREEN + "特に何も見つからなかった\n" + Color.END)
                elif key == "＠" :
                    if count == 0:
                        enem(4)
                    else:
                        enem(3)
                    count += 1
                elif key == "！":
                    eve()
                elif key == "＃":
                    treg(0)
                elif key == "？":
                    sear()
                else:
                    if key == "！" or key == "？" or key == "＃":
                        print(f'{Color.RED}{key}の残り探索回数は０です{Color.END}')
                state.point3[idx] = "＊"
            else:
                print(Color.RED+ "無効な記号です"+ Color.END)
                print(Color.RED+ "もう一度入力してください（記号は大文字です）"+ Color.END)
    if state.hp <= 0:
        return 1
    return 0
 
def MainGame():
    flg = game(1)
    if flg == 1:
        print(f"hpが0になった\n{Color.RED}あなたは１フロア目で敗北した{Color.END}")
        return
    print(f'{Color.YELLOW}フロア１をクリアした　{Color.BLUE}フロア２へ移動…{Color.END}')
    flg = game(2)
    if flg == 1:
        print(f"hpが0になった\n{Color.RED}あなたは２フロア目で敗北した{Color.END}")
        return
    print(f'{Color.YELLOW}フロア２をクリアした　{Color.BLUE}フロア３へ移動…{Color.END}')
    flg = game(3)
    if flg == 1:
        print(f"hpが0になった\n{Color.RED}あなたは３フロア目で敗北した{Color.END}")
        return
    print("最深部まで到達した")
    print(Color.GREEN + "！！クリア！！" + Color.END)

MainGame()

