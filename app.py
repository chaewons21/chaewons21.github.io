import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
y = 100 * (np.heaviside(t, 1) - np.exp(-2*t) - np.exp(-3*t)) + 100

plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Step Response')
plt.grid(True)
plt.show()