import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 2)
x = np.arange(0, 4*np.pi, 0.1)
ax[0, 0].plot(x, np.sin(x))
ax[1, 0].plot(x, np.cos(x))
ax[0, 1].plot(x, np.log(x))
ax[1, 1].plot(x, x)
plt.show()