import math

def simulate_motion():
    print("=== MatrixMotion 物理模擬器（第一階段） ===")
    
    # 1. 設定初始物理參數
    m = float(input("請輸入物體質量 (kg): "))
    x0 = float(input("請輸入初始 X 座標 (m): "))
    y0 = float(input("請輸入初始 Y 座標 (m): "))
    vx0 = float(input("請輸入初始 X 速度 (m/s): "))
    vy0 = float(input("請輸入初始 Y 速度 (m/s): "))
    
    # 假設一個定力（例如重力或風力），單位為牛頓 (N)
    fx = float(input("請輸入 X 方向受力 (N)，無受力請打 0: "))
    fy = float(input("請輸入 Y 方向受力 (N)，無受力請打 0: "))
    
    # 模擬參數
    t = 0.0
    dt = 0.1 # 時間間隔 (秒)
    total_time = 2.0 # 總模擬時間 (秒)
    
    x, y = x0, y0
    vx, vy = vx0, vy0
    
    print("\n" + "-"*50)
    print(f"{'時間(s)':<8}{'位置(X, Y)':<18}{'動量(Px, Py)':<20}{'角動量(L)'}")
    print("-"*50)
    
    # 2. 開始時間步進模擬 (Time-stepping simulation)
    while t <= total_time:
        # 計算動量 P = m * v
        px = m * vx
        py = m * vy
        
        # 計算二維角動量 L = x * py - y * px (外積概念)
        L = x * py - y * py
        
        # 顯示當前狀態
        print(f"{t:<8.1f}({x:<6.2f}, {y:<6.2f}) ({px:<8.2f}, {py:<8.2f}) {L:.2f}")
        
        # 利用動量衝量定理更新速度: F * dt = m * dv -> dv = (F / m) * dt
        vx += (fx / m) * dt
        vy += (fy / m) * dt
        
        # 更新位置: dx = v * dt
        x += vx * dt
        y += vy * dt
        
        t += dt

if __name__ == "__main__":
    simulate_motion()
