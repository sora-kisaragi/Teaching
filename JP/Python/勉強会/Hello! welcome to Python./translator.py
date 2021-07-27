#coding:utf-8
from googletrans import Translator

tr = Translator()

Japanese = input("日本語を入力して下さい -> ")
English = tr.translate(Japanese, src = "ja" , dest = "en").text

print("英語に翻訳 -> " + English)
