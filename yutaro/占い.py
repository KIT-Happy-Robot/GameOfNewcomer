import tkinter as tk
import tkinter.messagebox as mb
import random

fortune_list=[["大吉","[大吉]\n念願だった夢が叶います！"],
             ["吉","[吉]\n素敵な出会いがあります"],
             ["中吉","[中吉]\n多分良いことがあるでしょう"],
             ["凶","[凶]\nイライラしてはいけません"],
             ["大凶","[大凶]\nまあ人生こんなもんです（笑）"]]
def tell():
    rand_ft=random.randrange(len(fortune_list))
    r_ft=fortune_list[rand_ft]
    mb.showinfo(r_ft[0],r_ft[1])


root = tk.Tk()
root.title("占いアプリ")
root.geometry("640x480")

desc_label=tk.Label(text="あなたの運勢を占います。ぼたんをくりっくしてください",bg="#ccddff")
desc_label.pack(pady=80,ipady=30,ipadx=40,side="top")

button=tk.Button(text="あなた運勢を占う",width=20,height=2,command=tell)
button.pack(ipady=20)

root.mainloop()