import numpy as np

# Faça um programa que aplique um offset informado pelo usuário em uma banda
# Em alguns casos, o resultado pode ultrapassar o range de uma imagem de 8 bits (entre 0 e 255) force para ficar dentro do range (e.g. -50 → 0, e 270 → 255)

# criar a banda
banda = np.arange(100).reshape([10,10])
print(banda)
# definir o offset
offset = 200
# aplicar o offset
banda += offset
banda[banda > 255] = 255
banda[banda < 0] = 0
print(banda)
# desenhar na tela
import matplotlib.pyplot as plt
plt.imshow(banda, cmap='gray')
plt.show()
