import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag



t = np.linspace(0, 37.9, 200*37.9)
probkowanie=200
dane = pd.read_csv(r"C:\Users\acer-komp\Desktop\kc\sub-01_trial-07.csv", delimiter=',', engine='python')
sygnal = dane["kol2"]


przefiltrowany = ag.pasmowozaporowy(sygnal, probkowanie, 49, 51)
przefiltrowany2 = ag.pasmowoprzepustowy(przefiltrowany, probkowanie, 1, 50)

plt.subplot(2, 1, 1)
plt.plot(t, sygnal)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.subplot(2, 1, 2)
plt.plot(t, przefiltrowany2)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [-]')
plt.show()
