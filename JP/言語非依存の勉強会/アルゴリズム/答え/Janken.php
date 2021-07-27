<?php

// 勝敗判定関数
function Judge($a, $b) {
    if ($a > 2 || $b > 2) {
        $a = (int)($a / 3);
        $b = (int)($b / 3);
    }
    return ($a - $b + 3) % 3;
}

// 手のリスト
$hand_list = array(
    0 => 'グー',
    1 => 'チョキ',
    2 => 'パー',
);

// 結果リスト
$result_list = array(
    2 => 'あなたの勝ちです',
    1 => 'あなたの負けです',
    0 => 'あいこです',
    -1 => '不明',
);

// 手が送信されたとき勝負を実行
if (isset($_POST['you'])) {
    // 整数型にキャスト(不正な値をエラー無しに防ぐ効果もある)
    $you = (int)$_POST['you'];
    // コンピュータの手を選出
    $com = array_rand($hand_list);
    if (!isset($hand_list[$you])) {
        // 不正な値のときは自分の手を「？」、結果を「不明」にする
        $hand_list[$you = $result = -1] = '？';
    } else {
        // 正しい値のときは関数に渡す
        $result = judge($you, $com);
    }
}

// ヘッダー送信
header('Content-Type: application/xhtml+xml; charset=utf-8');

?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja">
  <head>
    <title>じゃんけんゲーム</title>
    <style type="text/css">
      label { display: block; }
    </style>
  </head>
  <body>
    <h1>じゃんけん</h1>
    <form action="" method="post">
      <label><input type="radio" name="you" value="0" checked="checked" />グー</label>
      <label><input type="radio" name="you" value="1" />チョキ</label>
      <label><input type="radio" name="you" value="2" />パー</label>
      <label><input type="submit" value="勝負！" /></label>
    </form>
<?php if (isset($result)): ?>
    <h1>勝負！</h1>
    <p>
      あなた： <?=$hand_list[$you]?><br />
      コンピュータ: <?=$hand_list[$com]?><br />
      <?=$result_list[$result]."\n"?>
    </p>
<?php endif; ?>
  </body>
</html>