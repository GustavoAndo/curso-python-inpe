import extrair_dados
import matplotlib.pyplot as plt

populacao_masc = [int(x[1]) * -1 for x in extrair_dados.dados()]
populacao_fem = [int(x[2]) for x in extrair_dados.dados()]
idades = [x[0] for x in extrair_dados.dados()]

x_pos = [ x for x in range( len(idades) ) ]

plt.barh(x_pos, populacao_masc, align='center',
        color='lightblue', linewidth=2, edgecolor='black')

plt.barh(x_pos, populacao_fem, align='center',
        color='orange', linewidth=2, edgecolor='black')

plt.xticks([ -9000000, -6750000, -4500000, -2250000, 0, 2250000, 4500000, 6750000, 9000000 ],
           [ "9 milhões", "6,75 milhões", "4,5 milhões", "2,25 milhões", "0", "2,25 milhões", "4,5 milhões", "6,75 milhões", "9 milhões" ] )
plt.yticks(x_pos, idades) 

plt.title("Distribuição da População do por sexo segundo os grupos de idade - Brasil - 2010")

plt.ylabel("Idades")
plt.xlabel("População")

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()