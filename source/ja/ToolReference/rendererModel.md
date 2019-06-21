﻿
# 描画-モデル

## 概要

描画の設定で、「モデル」を選択した場合の描画及びパラメーターについて説明します。

「モデル」を選択すると、外部から読み込んだ3Dモデルが表示されます。

モデルに使用する色に関する画像は描画共通の色/歪み画像を使用しています。モデルによっては深度書き込み、深度テストを有効にしないと表示がおかしくなることがあります。

![](../../img/Reference/renderModel.png)

## パラメーター

### モデル

表示に使用するFBX(.fbx)、metasequoiaファイル(.mqo)、もしくは、Effekseer用モデルファイル(.efkmodel)を指定します。 .efkmodel以外を指定した場合、指定したファイルと同じディレクトリに.efkmodelが生成されます。他アプリケーションでエフェクトを再生する場合、 この生成されたファイルが必要です。

アニメーション付きのFBX(.fbx)を読み込むこともできます。 FBXファイルで一番目に設定されているアニメーションが再生されます。

### 法線画像

3Dモデルに使用する法線画像を指定します。

### ライティング

モデルが光源の影響を受けるかどうか指定します。

### カリング

モデルの表示する面の方向を指定します。

### 全体色

モデル全体の色調を指定します。