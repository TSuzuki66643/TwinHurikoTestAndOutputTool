# ２重振り子軌道生成ツール / TwinHurikoTestAndOutputTool

その昔、何かのセミナーでこのコードをもらってきたのだが、ローカルで動かせるようにしたのがこれ。<br/>

## 説明/Description
このコードを実行することで2重振り子の動きと軌跡を確認できるgifファイルを生成する。<br/>
生成先は当該.pyファイルのあるフォルダーと同階層になる。

## 環境/Environment
Python環境のほか、以下のモジュールがimportされている。

```python
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation
from IPython.display import HTML #未使用のはず。将来的には廃止する予定
```

## 設定/Settings
以下は設定項目である。
```python
#30行目から
G = 9.8   # 重力加速度の大きさ[m/s^2]
L1 = 1.3  # 振り子１の長さ[m]
L2 = 0.4  # 振り子２の長さ[m]
M1 = 1.3  # 振り子１のおもりの質量[kg]
M2 = 0.4  # 振り子２のおもりの質量[kg]

# 時間の設定（0から15までを0.05刻みのデータを配列 t に格納）
dt = 0.05
t = np.arange(0.0, 15, dt)　#(起点sec.,終点sec.,間隔sec.)

### 振り子１の初期条件 #######################################
th1 =  90.0 #角度
w1 =   0.0　#わからん
### 振り子２の初期条件 #######################################
th2 = 191.0
w2 =   0.0

time_template = 'time = %.2fs'#時間タイマーの表示桁数

#最終行
ani.save('filename.gif',writer='pillow',fps=30) #filenameとfpsはお好みで
```


