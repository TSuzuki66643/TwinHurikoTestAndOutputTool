from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation


def derivs(state, t):   # 右辺の関数の定義
                        # state=[th1, w1, th2, w2]👈
    dydx = np.zeros_like(state)   # dydxの初期化
    dydx[0] = state[1]            # dydx[0]=d/dt th1

    del_ = state[2] - state[0]
    den1 = (M1 + M2)*L1 - M2*L1*cos(del_)*cos(del_)
    dydx[1] = (M2*L1*state[1]*state[1]*sin(del_)*cos(del_) +
               M2*G*sin(state[2])*cos(del_) +
               M2*L2*state[3]*state[3]*sin(del_) -
               (M1 + M2)*G*sin(state[0]))/den1             # dydx[1]=d/dt w1

    dydx[2] = state[3]            # dydx[2]=d/dt th2

    den2 = (L2/L1)*den1
    dydx[3] = (-M2*L2*state[3]*state[3]*sin(del_)*cos(del_) +
               (M1 + M2)*G*sin(state[0])*cos(del_) -
               (M1 + M2)*L1*state[1]*state[1]*sin(del_) -
               (M1 + M2)*G*sin(state[2]))/den2             # dydx[3]=d/dt w2

    return dydx

G = 9.8   # 重力加速度の大きさ[m/s^2]
L1 = 1.3  # 振り子１の長さ[m]
L2 = 0.4  # 振り子２の長さ[m]
M1 = 1.3  # 振り子１のおもりの質量[kg]
M2 = 0.4  # 振り子２のおもりの質量[kg]

# 時間の設定（0から30までを0.05刻みのデータを配列 t に格納）
dt = 0.05
t = np.arange(0.0, 15, dt)

### 振り子１の初期条件 #######################################
th1 =  90.0
w1 =   0.0
### 振り子２の初期条件 #######################################
th2 = 191.0
w2 =   0.0

# 初期状態の設定　（state の初期状態）
state = np.radians([th1, w1, th2, w2])

# 常微分方程式を解く（scipyライブラリの中の「odeint」の使用）
y = odeint(derivs, state, t)

# 結果のプロット（θ1とθ2の時間依存性を表示）
fig1 = plt.figure()
ax1  = fig1.add_subplot(111)
ax1.plot(t, y[:, 0], label= '$\\theta_1$')   # th1のプロット
ax1.plot(t, y[:, 2], label= '$\\theta_2$')   # th2のプロット
ax1.legend()
#plt.show()

# アニメーションの作成（以下は理解できなくても大丈夫です。）
x1 =  L1*sin(y[:, 0])         # リストの0番目、θ１を取り出しています。
y1 = -L1*cos(y[:, 0])

x2 =  L2*sin(y[:, 2]) + x1    # リストの2番目、θ2を取り出しています。
y2 = -L2*cos(y[:, 2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
ax.set_aspect('equal')
ax.grid()

line,  = ax.plot([], [], 'o-', lw=2)
line2, = ax.plot([],[], '-', color='red')

thi2x, thi2y = [], []

# タイマーを表示するために追加
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    line2.set_data([], [])
    #　これもタイマー用の初期化
    time_text.set_text('')
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    thi2x.append(x2[i])
    thi2y.append(y2[i])

    line.set_data(thisx, thisy)
    line2.set_data(thi2x, thi2y)
    # タイマー更新用
    time_text.set_text(time_template % (i*dt))
    return line

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(y)),
                              interval=40, init_func=init)



from IPython.display import HTML
ani.save('005.gif',writer='pillow',fps=30)