import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# 전달함수의 분자와 분모 계수
num = [100]
den = [1, 5, 6]  # (s+2)(s+3) 확장

# 전달함수 생성
H = signal.TransferFunction(num, den)

# 주파수 응답 계산
w, mag, phase = signal.bode(H)

# 보드선도 그리기
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.semilogx(w, mag)  # 주파수에 따른 게인 (dB)
ax1.set_xlabel('Frequency [rad/s]')
ax1.set_ylabel('Gain [dB]')
ax1.set_title('Bode Plot - Gain')

ax2.semilogx(w, phase)  # 주파수에 따른 위상 (도)
ax2.set_xlabel('Frequency [rad/s]')
ax2.set_ylabel('Phase [degrees]')
ax2.set_title('Bode Plot - Phase')

plt.tight_layout()
plt.show()
