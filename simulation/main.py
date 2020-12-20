 
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sp

time = np.linspace(0, 10, 500)
pwmH = np.linspace(0, 10, 500)
pwmL = np.linspace(0, 10, 500)

sin = np.sin(time)
sawtooth = 1.1*sp.sawtooth(2 * np.pi * time * 2)

for index, value in enumerate(time):
    # For positive cicles 
    if( sin[index] > 0 ): 
        if( sin[index] > sawtooth[index] ):
            pwmH[index] = 1
            pwmL[index] = -1
        else:
            pwmH[index] = 0
            pwmL[index] = 0
    # For negatives cicles
    if( sin[index] < 0 ): 
        if( sin[index] < sawtooth[index] ):
            pwmH[index] = -1
            pwmL[index] = 1
        else:
            pwmH[index] = 0
            pwmL[index] = 0


fig, ax = plt.subplots()

ax.plot( time, pwmH )
ax.plot( time, pwmL )
# ax.plot( time, sawtooth )
ax.plot( time, sin )


plt.grid(True)
plt.show()

