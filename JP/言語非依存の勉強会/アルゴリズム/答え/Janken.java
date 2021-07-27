import java.util.Random;
import java.util.Scanner;

public class Janken
{

    private static int m_player_1 = 0;
    private static int m_player_2 = 0;
    // true = ループ
    private static boolean GameLoop = true;

    // Input用変数
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args)
    {

        // じゃんけんゲーム開始
        while (GameLoop)
        {
            // 手を入力
            m_player_1 = Player_Input();
            m_player_2 = COM_Input();
            int num = Judge(m_player_1, m_player_2);

            // あいこの場合と続けて遊ぶ場合はループ
            if (num == 0)
            {
                System.out.println("もう一度！");
            } else
            {
                GameLoop = nextGame();
            }
        }

        // ゲームの終了
        sc.close();
        System.exit(0);

    }

    /*
     * Player1を基準にじゃんけんのパターンを想定
     * 1: (P_1 - P_2 + 3) % 3 = 0 の時は、あいこ
     * 2: (P_1 - P_2 + 3) % 3 = 2 の時は、敗北
     * 3: (P_1 - P_2 + 3) % 3 = 1 の時は、勝利
     *
     *  return = 勝敗(int);
     */
    public static int Judge(int p_1, int p_2)
    {
        int judge = ((p_1 - p_2 + 3) % 3);

        // 見えやすくするための改行
        System.out.println();

        switch (judge) {
        case 0:
            System.out.println(" [ あいこ ]");
            break;
        case 1:
            System.out.println(" [ 負け ]");
            break;
        case 2:
            System.out.println(" [ 勝ち ]");
            break;
        }

        // 見えやすくするための改行
        System.out.println();

        return judge;
    }

    /*
     * キーボード入力で0,1,2 を入力すると自身の手が決定する
     * 0,1,2以外の入力値の場合は再入力
     * */
    public static int Player_Input()
    {

        System.out.println("じゃんけん あなたの手は？\n" + "0 = グー\n" + "1 = チョキ\n" + "2 = パー\n" + " ↓ ");
        int hand_num = sc.nextInt();

        while (!((hand_num <= 3) && (hand_num >= 0)))
        {
            System.out.println("もう一度正しい手を入力してください");
            hand_num = sc.nextInt();
        }

        System.out.print("あなた の 手は →");
        switch (hand_num) {
        case 0:
            System.out.println("グー");
            break;
        case 1:
            System.out.println("チョキ");
            break;
        case 2:
            System.out.println("パー");
            break;
        }

        return hand_num;
    }

    /*
     * COMの手をランダムで入力
     * */
    public static int COM_Input()
    {
        Random rand = new Random();
        int hand_num = rand.nextInt(3);

        System.out.print("COM の 手は →");
        switch (hand_num) {
        case 0:
            System.out.println("グー");
            break;
        case 1:
            System.out.println("チョキ");
            break;
        case 2:
            System.out.println("パー");
            break;
        }

        return hand_num;
    }

    /*
     * 勝敗決定後 もう一度遊ぶかどうかを決める
     * */
    public static boolean nextGame()
    {
        System.out.println("もう一度あそぶ？\n" + "はい -> 0\n" + "いいえ -> それ以外");
        int _n = sc.nextInt();

        // 見えやすくするための改行
        System.out.println();

        // はいが選ばれたときだけGameLoopを続行する
        if (_n == 0)
        {
            return true;
        }

        return false;

    }

}