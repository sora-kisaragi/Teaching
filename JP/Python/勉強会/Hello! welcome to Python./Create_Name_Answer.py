#coding:utf-8
# 問１ Googleの翻訳ライブラリを利用します
from googletrans import Translator
# 問2 インスタンスの生成
tr = Translator()


# 命名規則に従って翻訳する関数
def create_name(what_ja,be_ja):

    # 問3 何をしたい？を日本語で受け取り、英語に翻訳する
     what_en = tr.translate(what_ja, src="ja", dest="en").text

    # 問4 どうしたい？を日本語で受け取り、英語に翻訳する
    be_en = tr.translate(be_ja, src="ja", dest="en").text

    #　ここは命名規則に従って変換する処理 後で見てね
    # .capitalizer() = String型の文字列の先頭を大文字に、他を小文字に変換する関数
    # .lower() = String型の文字列を、全て小文字に変換する関数
    # 0 = パスカルケース PascalCase
    # 1 = キャメルケース camelCase
    # 2 = スネークケース snake_case
    # 3 = パスカルスネークケース Pascal_Snake
    while True:

        case = input(" 0. PascalCase \n 1. camelCase \n 2.snake_case \n 3.Pascal_Snake \n 利用する命名パターンを選択して下さい\n ")

        if case == "0":
            text = what_en.capitalize() + be_en.capitalize()
        elif case == "1":
            text = what_en.lower() + be_en.capitalize()
        elif case == "2":
            text = what_en.lower() + "_" + be_en.lower()
        elif case == "3":
            text = what_en.capitalize() + "_" + be_en.capitalize()
        else:
            print("もう一度入力してください \n")
            continue
        print("結果 -> " + text)
        break



print("こんにちは！ 簡単名付け装置です！")
print("使いたい単語を質問に従って入力してね\n")

what_ja = input("何を？\n")
be_ja = input("どうする？\n")

# 問5 作った関数を呼び出して、入力された文字を引数に設定して下さい。
create_name(what_ja,be_ja)


    