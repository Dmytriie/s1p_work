import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import sys
import matplotlib.cm as cm
import math

Crffile = sys.argv[1]
Indfile = sys.argv[2]

#Indset = np.genfromtxt( Indfile, skip_header = 1997, skip_footer = (1845), delimiter = ',') #only for the VSWR
#Indset = np.reshape (Indset, (len(Indset), 3) ) #only for the VSWR
Indset = np.genfromtxt( Indfile, skip_header = 3, skip_footer = (0), delimiter = ',')
Indset = np.reshape (Indset, (len(Indset), 3) )

#Crfset = np.genfromtxt( Crffile, skip_header = 1628, skip_footer = (4001-1643), delimiter = ',') #only for the VSWR
#Crfset = np.reshape (Crfset, (len(Crfset), 3) ) #only for the VSWR
Crfset = np.genfromtxt( Crffile, skip_header = 1433, skip_footer = (2170), delimiter = ',')
Crfset = np.reshape (Crfset, (len(Crfset), 3) )

def VSWR(array):
	return  np.divide((1+ np.abs(array)), (1 - np.abs(array)))

def LOSS(array):
	return 20*np.log10(np.abs(array))
	
matplotlib.rcParams.update({'font.size': 12})
matplotlib.rcParams['figure.figsize'] = (8, 5)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel ('Frequency, MHz')
ax.set_ylabel ('VSWR')
ax.set_title('VSWR comparison')
ax.set_xticks(np.arange(3.5E8, 4.6E8, step=0.1E8))
ax.set_xticks(np.arange(3.5E8, 4.6E8, step=0.02E8), minor = True)
ax.set_yticks(np.arange(10, 35, step=2))
ax.set_yticks(np.arange(10, 35, step=0.5), minor = True)
ax.grid(which = 'both')
#ax.plot(Indset[:, 0], VSWR(Indset[:, 1]),   label="MCL SXBP-404") #only for the VSWR
#ax.plot(Crfset[:, 0], VSWR(Crfset[:, 1]), label="This work")  #only for the VSWR
ax.plot(Indset[:, 0], LOSS(Indset[:, 1]),  label="MCL SXBP-404")
ax.plot(Crfset[:, 0], LOSS(Crfset[:, 1]),  label="This work") 

ax.legend( loc='center left', borderaxespad=0.,   prop={'size': 10}, bbox_to_anchor=(0.75, 0.6))
plt.tight_layout()
plt.savefig('Losses.pdf', bbox_inches='tight')	
plt.show()

