# 描画モード 

エディターでは、パーティクルをいくつかの描画モードで表示することができ、編集したエフェクトのさまざまな側面をデバッグするのに便利です。

## 通常

```eval_rst
.. image:: ../../img/Reference/DrawMode_Normal.png
   :align: center
```

これはデフォルトの描画モードです。エンジンでレンダリングされるのと同じようにパーティクルが表示されます。

## ワイヤーフレーム

```eval_rst
.. image:: ../../img/Reference/DrawMode_Wireframe.png
   :align: center
```

パーティクルのワイヤーフレームを表示します。

## ワイヤーフレーム＋法線

```eval_rst
.. image:: ../../img/Reference/DrawMode_WireframeNormal.png
   :align: center
```

ワイヤーフレームを重ねたテクスチャパーティクルを表示します。

## オーバーレイ

```eval_rst
.. image:: ../../img/Reference/DrawMode_Overdraw.png
   :align: center
```

このモードは、最適化の際に便利です。パーティクルの透明な "シルエット"を描画します。
この透明な色が蓄積されることで、複数のパーティクルが重なっている場所を簡単に見つけることができます。

パーティクルの過剰描画は通常、パフォーマンス問題の主な原因です。可能であれば、重なり合うパーティクルの量を減らすことで、オーバードローを減らしたいでしょう。