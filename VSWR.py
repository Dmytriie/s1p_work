import numpy as np
import matplotlib.pyplot as plt
import sys

num_points = 4001
dataset = np.genfromtxt(sys.argv[1], skip_header = 5)
S11_abs = np.sqrt(np.add(np.square(dataset[:,1]), np.square(dataset[:,2]))) #Z^2 = sqrt (a^2 + b^2)
VSWR = np.divide(1 + S11_abs, 1 - S11_abs)

fig = plt.figure()
fig.add_subplot(211)
plt.title('S11')
plt.xlabel('Frequency, Hz')
plt.ylabel('S11')
plt.yscale('linear')
plt.grid(True)
plt.tight_layout()
plt.plot(dataset[:,0], S11_abs)

fig.add_subplot(212)
plt.title('VSWR')
plt.xlabel('Frequency (Hz)')#plt.savefig('ratio_CST.png')
plt.ylabel('VSWR')
plt.yscale('linear')
plt.plot(dataset[:,0], VSWR)
plt.grid(True)
plt.tight_layout()
plt.savefig(sys.argv[1] + '.pdf')
plt.show()
