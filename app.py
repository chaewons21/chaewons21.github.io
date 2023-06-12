streamlit
pandas
numpy
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

num = [100]
den = [1, 5, 6]  # (s+2)(s+3) 


H = signal.TransferFunction(num, den)


w, mag, phase = signal.bode(H)


fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.semilogx(w, mag) 
ax1.set_xlabel('Frequency [rad/s]')
ax1.set_ylabel('Gain [dB]')
ax1.set_title('Bode Plot - Gain')

ax2.semilogx(w, phase) 
ax2.set_xlabel('Frequency [rad/s]')
ax2.set_ylabel('Phase [degrees]')
ax2.set_title('Bode Plot - Phase')

plt.tight_layout()
plt.show()
