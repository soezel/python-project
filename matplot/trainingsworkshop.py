# http://85.214.241.203/

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1000)

plt.plot(x)

plt.gcf()
plt.savefig('matplot/Kundenauftrag0.png',dpi=30)
plt.show()