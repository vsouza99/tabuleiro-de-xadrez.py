import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

tabuleiro = np.tile([1, 0], (8, 4))
 
for i in range(tabuleiro.shape[0]):
    tabuleiro[i] = np.roll(tabuleiro[i], i % 2)

mapa_de_cores = ListedColormap(['#0096ff' , '#ffa900'])
plt.matshow(tabuleiro, cmap= mapa_de_cores)
plt.xticks([])
plt.yticks([])
plt.show()



