import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


num = [100]
den = [1, 5, 6]  # (s+2)(s+3) 확장

# 전달함수 생성
sys = signal.TransferFunction(num, den)

# 시간 범위 설정
t = np.linspace(0, 10, 1000)

# 시스템 응답 계산
t, y = signal.step(sys, T=t)

# 응답곡선 그리기
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()

