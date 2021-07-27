public class BubbleSort {
    public static void main(String args[]) {
        int a[] = {5,2,9,6,1};
        // aの内容を表示
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println();
        // バブルソート
        boolean flag = true; // 交換が発生したかどうか
        while (flag) {
            flag = false;
            // 先頭から順に隣接する逆順要素を交換する
            for (int i = 1; i < a.length; i++) {
                if (a[i-1] > a[i]) {
                    // a[i]とa[i-1]を交換
                    int w = a[i];
                    a[i] = a[i-1];
                    a[i-1] = w;
                    flag = true;
                }
            }
            // aの内容を表示
            for (int i = 0; i < a.length; i++) {
                System.out.print(a[i] + " ");
            }
            System.out.println();
        }
    }
}