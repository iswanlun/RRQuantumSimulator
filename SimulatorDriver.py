import numpy as np
import matplotlib.pyplot as plt
from SimulatorModule import simModule
from scipy import stats

slt = simModule()
data = []

for a in range(8, 16):
    for s in np.linspace(2, 5, num=5):
        data.append([a, s, slt.simulator(a, s, 5)])

x = []
y = []

for n in data:
    x.append((n[0] + n[1]))
    avg = (n[2][1] + n[2][3]) / 2
    y.append(avg)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
predict_y = [intercept + float(slope) * float(l) for l in x]

fig, ax = plt.subplots()

ax.plot(x, predict_y, 'k')
ax.scatter(x, y)

ax.set_ylabel("Fastest Quamtum")
ax.set_xlabel("Mean + std")
ax.set_title('Simulated fastest quantum vs Mean + Std')
ax.legend(('r={:.2f}'.format(r_value), 'Quantums'))
plt.show()
