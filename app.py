import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num = [100]
den = [1, 5, 6]  # (s+2)(s+3) 

sys = signal.TransferFunction(num, den)


w = np.logspace(-2, 2, 1000)


w, mag, phase = signal.bode(sys, w)

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.semilogx(w, mag)  
ax1.set_xlabel('Frequency [rad/s]')
ax1.set_ylabel('Gain [dB]')
ax1.set_title('Bode Plot - Gain')

ax2.semilogx(w, phase)  # 주파수에 따른 위상 (도)
ax2.set_xlabel('Frequency [rad/s]')
ax2.set_ylabel('Phase [degrees]')
ax2.set_title('Bode Plot - Phase')

plt.tight_layout()
plt.show()
