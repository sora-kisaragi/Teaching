import random


m_player_1 = int(0)
m_player_2 = int(2)



#  Player1を基準にじゃんけんのパターンを想定
#  1: (P_1 - P_2 + 3) % 3 = 0 の時は、あいこ
#  2: (P_1 - P_2 + 3) % 3 = 2 の時は、敗北
#  3: (P_1 - P_2 + 3) % 3 = 1 の時は、勝利
#   return = 勝敗(int);
def Judge(p1, p2):
    
    judge = ((p1 - p2 + 3) % 3)

    if judge == 0:
        print(" [ あいこ ] ")
    elif judge == 1:
        print(" [ 負け ] ")
    elif judge == 2:
        print(" [ 勝ち ] ")
    
    return judge

def Player_Input():

    print("じゃんけん あなたの手は？\n" + "0 = グー\n" + "1 = チョキ\n" + "2 = パー\n" + " ↓ ")
    hand_num = int(input())

    #入力範囲外の時
    while(not((hand_num <= 3) and (hand_num >= 0))):
        print("もう一度ただし手を入力してください")
        hand_num = int(input())
    
    print("あなたの手は ")
    if hand_num == 0:
        print("グー")
    elif hand_num == 1:
        print("チョキ")
    elif hand_num == 2:
        print("パー")
    
    return hand_num


def CPU_Input():
    hand_num = random.randint(1,3)

    print("CPUの手は ")
    if hand_num == 0:
        print("グー")
    elif hand_num == 1:
        print("チョキ")
    elif hand_num == 2:
        print("パー")
    
    return hand_num

def nextGame():
    print("もう一度あそぶ？\n" + "はい -> 0\n" + "いいえ -> それ以外")
    _n = int(input())

    if _n == 0:
        return True
    
    return False


def main():
    GameLoop = True
    while GameLoop == True:
        # 手を入力
        m_player_1 = Player_Input()
        m_player_2 = CPU_Input()
        num = Judge(m_player_1,m_player_2)

        if num == 0:
            print("もう一度！")
        else:
            GameLoop = nextGame()
        

main()
