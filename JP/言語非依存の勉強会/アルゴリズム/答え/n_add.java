import java.util.Scanner;

class n_add {
  public static void main(String[] args) {
    double answer = 0;
    int last_num = 100000000;
    var sisuu = 1e-9;

    // 数字の入力
    Scanner scan = new Scanner(System.in);
    System.out.print("好きな数字を入力してください > ");

    last_num = scan.nextInt();

    // 計測開始
    long startTime = System.nanoTime();

    // 計算処理
    // for (int i = 1; i <= last_num; i++){
    // answer += i + 1;
    // }
    answer = (0.5 * last_num) * (last_num + 1);

    // 計測終了
    long endTime = System.nanoTime();

    // 計測時間の差分を計算して表示
    // 10^-9をかけてナノ秒から秒に変換 差は１億倍
    System.out.println("経過時間 : " + ((endTime - startTime) * sisuu) + "秒");

    System.out.println("合計 : " + answer);

  }
}