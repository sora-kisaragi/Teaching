 # バブルソートを行う関数(data=配列データ、n=dataの要素数）
def bubble_sort(data, n):
    for i in range(n):                                      # i=0からnまでのループ
        for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
            if data[j-1] > data[j]:                         # 隣り合う値を比較
                data[j], data[j-1] = data[j-1], data[j]     # 交換
    return data
 
# ランダムなサンプルデータを使って関数を実行する
y = [5,2,9,6,1]
print(y)                            # ソート前のデータを表示
y = bubble_sort(y, len(y))
print(y)                            # ソート後のデータを表示