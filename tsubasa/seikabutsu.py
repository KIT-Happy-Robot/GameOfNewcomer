import random
def 'mirionaire_quiz()'
    questions = 
        {  "question": "金沢工業大学の設立年はいつですか？",
            "choices": ["1949年", "1951年", "1965年", "1970年"],
            "correct_answer": 2
        },
        {
            "question": "金沢工業大学のキャンパスは何ヶ所ありますか？",
            "choices": ["1ヶ所", "2ヶ所", "3ヶ所", "4ヶ所"],
            "correct_answer": 3
        },
        {
            "question": "金沢工業大学の学部数はいくつですか？",
            "choices": ["4学部", "6学部", "8学部", "10学部"],
            "correct_answer": 0
        },
        {
            "question": "金沢工業大学の学生数は約何人ですか？",
            "choices": ["3,000人", "5,000人", "8,000人", "10,000人"],
            "correct_answer": 2
        },
        {
            "question": "金沢工業大学の創設者は誰ですか？",
            "choices": ["泉屋利吉", "鈴木寿一", "伊藤一彦", "大和健二"],
            "correct_answer": 0
        },
        {
            "question": "金沢工業大学の最も古い学部は何学部ですか？",
            "choices": ["工学部", "情報学部", "都市デザイン学部", "生命理工学部"],
            "correct_answer": 0
        },
        {
            "question": "金沢工業大学の略称は何ですか？",
            "choices": ["KU", "KUT", "KIT", "KIU"],
            "correct_answer": 2
        },
    score = 0
    while True:
        question = random.choice(questions)
        print(question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")

        answer = input("選択肢の番号を入力してください (qで終了): ")

        if answer.lower() == "q":
            break
        try:
            answer = int(answer) - 1
        except ValueError:
            print("数値を入力するか、qで終了してください。")
            continue
        
        if answer < 0 or answer >= len(question["choices"]):
            print("選択肢の番号を入力してください。")
            continue
        elif answer == question["correct_answer"]:
            print("正解！\n")
            score += 1
        else:
            print("不正解！ゲームオーバー！\n")
            break
        print('終わり')