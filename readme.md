These two files were created during my work with bandpass filter for the new ESR 410 MHz Schottky cavity
In order to finish signal processing line we decided to order industrial bandpass filter and while it goes to the GSI we created handmade one :)
Parameters which allow you to compare twofilters are VSWR and loss (also S-parameters)

VSWR.py: For a radio (transmitter or receiver) to deliver power to an antenna, the impedance of the radio and transmission line must be well matched to the antenna's 
impedance. The parameter VSWR is a measure that numerically describes how well the antenna is impedance matched to the radio or transmission line it is connected to.
VSWR stands for Voltage Standing Wave Ratio, and is also referred to as Standing Wave Ratio (SWR). VSWR is a function of the reflection coefficient, 
which describes the power reflected from the antenna.

loss.py: In case the two measurement ports use the same reference impedance, the insertion loss (IL) is the reciprocal of the magnitude of the transmission coefficient |S21|
expressed in decibels. It is thus given by:
IL = − 20 log10 |S21| dB.
It is the extra loss produced by the introduction of the device under test (DUT) between the 2 reference planes of the measurement. 
The extra loss may be due to intrinsic loss in the DUT and/or mismatch. In case of extra loss the insertion loss is defined to be positive. 
The negative of insertion loss expressed in decibels is defined as insertion gain and is equal to the scalar logarithmic gain.

Both files contain simple script with matplotlib.pyplot to show/save the plots from datasets
