import numpy as np

# offset é um número real que é somado a todos os pixels de uma banda.
# ganho é um número real que é multiplicado por todos os pixels da banda.
# Suponha uma banda de uma imagem armazenada em uma matriz de 10 linhas e 10 colunas

banda = np.zeros([10,10])
# modificar alguns pixels da banda
banda[2,2] = banda[2,-3] = banda[4,4] = banda[4,5] = banda[6,1] = banda[6,-2] = banda[7,2:8] = 0.25
# para mostrar a matriz como uma imagem
import matplotlib.pyplot as plt
plt.imshow(banda, vmax=255)
plt.show()
# ao não perceber nenhum conteúdo na imagem, pense num ganho ou offset para aplicar na imagem
banda *= 500
plt.imshow(banda, vmax=255)
plt.show()