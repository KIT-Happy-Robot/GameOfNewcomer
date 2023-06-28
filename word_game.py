import json
import random

def int_random(min, max):
    return int(random.uniform(min, max))


def read_json(url):
    json_open = open(url, 'r')
    json_load = json.load(json_open)
    json_open.close()
    return json_load

def write_json(url, data):
    json_open = open(url, 'w')
    json.dump(data, json_open)
    json_open.close()

write_json('./user_data.json', "test")


plya_limit = 5
character_limit = 7
json_url = './word_data_json/word' + str(int_random(1, 6)) + ".json"

class Word:
    def __init__(self, url):
        word_json = read_json(url)
        word_json_len = len(word_json)
        random_number = int_random(0, word_json_len)
        while len(word_json[random_number]["name"]) != character_limit:
            random_number = int_random(0, word_json_len)
        else:
            ans = word_json[random_number]

        self.english = ans["name"].lower()
        self.japanese = ans["description"]


    def getEnglishWord(self):
        return  self.english
    
    def getJapaneseWord(self):
        return self.japanese
    


def check_str(i, e, ans):
    if ans[i] == e:
        return e.upper()

    elif ans.find(e) != -1:
        return e

    else:
        return "_"



def get_str(count):
    print( count+1,"/", plya_limit,"回目")
    input_str = input(str(character_limit)+"文字の英単語を入力してください : ")

    if len(input_str) != character_limit:
        print("注意:入力は", character_limit ,"文字です")
        return get_str(count)
    
    for e in input_str:
        if not(65 <= ord(e) <= 90 or 97 <= ord(e) <= 122):   
            print("注意:入力は半角英字のみです")
            return get_str()      
         
    return input_str.lower()


def game():
    print(" 単語あてゲームです。",character_limit,"文字の英単語を入力すると\n大文字:文字も位置も正解\n小文字:使われているが文字の位置が違う\n\"_\":使われていない\nの3種類で返されます。",plya_limit, "回以内に当ててください")

    return_str = [[] for i in range(plya_limit)]
    wr = Word(json_url)

    ans_English = wr.getEnglishWord()
    ans_Japanese = wr.getJapaneseWord()
    if input("始めるにはキーを押してください") == "happy":
        print("ans:", ans_English)

    for count in range(plya_limit):
        input_str = get_str(count)
        if ans_English == input_str:
            print("正解です！回数:", count+1,"/", plya_limit,)
            break

        for i, e in enumerate(input_str):
            return_str[count].append(check_str(i, e, ans_English))

        for i in range(count+1):
            print( return_str[i])

    else:
        print("GAME OVER\n正解は",ans_English,"です")
        data = {
        
        }
        print("日本語：" + ans_Japanese)




game()
