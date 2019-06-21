﻿# Fカーブ

## 概要

グラフを用いて、フレームごとに値を設定できる機能です。

![](../../img/Reference/fcurve_ja.png)

## 操作方法

### グラフの表示

各項目(位置、回転等)にてFカーブを指定することにより、Fカーブウインドウにグラフが表示されます。

![](../../img/Reference/fcurve_select_ja.png)

画面の左に表示されているツリーの項目を選択するとFカーブが表示されます。Shiftを押しながら選択することで、複数同時に選択することもできます。

<iframe width="560" height="315" src="https://www.youtube.com/embed/XrENrALqa-Q" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen=""></iframe>

### グラフの移動・拡大縮小

<table>

<tbody>

<tr>

<td>グラフの移動</td>

<td>グラフ上で、マウスの右ボタンを押しつつ、マウスを移動</td>

</tr>

<tr>

<td>横方向・拡大縮小</td>

<td>グラフ上で、Ctrlを押しつつ、マウスホイールを回転</td>

</tr>

<tr>

<td>縦方向・拡大縮小</td>

<td>グラフ上で、Altを押しつつ、マウスホイールを回転</td>

</tr>

</tbody>

</table>

### キーの追加

マウスで線上をダブルクリックすることでキーを追加できます。

### キーの削除

マウスでキーをダブルクリックすることでキーを削除できます。

### キーの選択

マウスを左クリックすることで選択できます。

### キーの移動

キー選択した後、マウスの左ボタンを押したままマウスを移動することで移動できます。 同じように、カーブの制御用のキーも移動させることができます。

### アンカーの展開,縮小

キーを選択し、アンカーの展開や縮小を押すことでアンカーの位置を自動的に指定できます。 アンカーの展開を押すとアンカーが展開して線が滑らかになります。 アンカーの縮小を押すとアンカーとポイントの位置が一致して急に値が変化するようになります。

### 全表示

グラフのラベルをダブルクリックするとグラフ全体が表示されます。

![](../../img/Reference/fcurve_show_entire.png)

## パラメーター

### フレーム

キーごとに設定します。キーのフレームを指定します。

### 値

キーごとに設定します。キーの値を指定します。

### 補完

キーごとに設定します。キーとキーの間の補完方法を指定します。

### 先頭

グラフごとに設定します。グラフの左端より前のグラフの値の設定方法を指定します。

### 末尾

グラフごとに設定します。グラフの右端より後のグラフの値の設定方法を指定します。

### サンプリング

グラフごとに設定します。実際に再生するときに、何フレームごとの値を使用して表示するか指定します。小さいほどメモリは使いますが、グラフの形状に近い値を使用します。

### 左x,y

キーごとに設定します。キーのカーブ制御の左ハンドルの位置を指定します。

### 右x,y

キーごとに設定します。キーのカーブ制御の右ハンドルの位置を指定します。

### オフセット最大,最小

グラフごとに設定します。値を使用するときにオフセットの範囲で、ランダムに値を上下にグラフをずらします。