import time

first_num = 0
last_num = int(input("好きな数字を入力して下さい -> "))

t1 = time.time() 

# 100,000,000まで加算
# 計測時間 秒
# for i in range(last_num):
#     first_num += i + 1
#     print("\rcount " + str(i), end='')

# 100,000,000まで加算
# 計測時間 秒
first_num = (0.5 * last_num) * (last_num + 1)

t2 = time.time()
elapsed_time = t2-t1


print(f"\n結果 -> {first_num}")

print(f"経過時間：{elapsed_time}")


