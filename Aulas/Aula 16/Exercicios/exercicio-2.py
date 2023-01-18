import extrair_dados
import matplotlib.pyplot as plt

populacao_fem = [int(x[1]) for x in extrair_dados.dados()]
idades = [x[0] for x in extrair_dados.dados()]

x_pos = [ x for x in range( len(idades) ) ]

plt.barh(x_pos, populacao_fem, align='center',
        color='lightblue', linewidth=2, edgecolor='black')

plt.xticks([ 0, 2250000, 4500000, 6750000, 9000000 ],
           [ "0", "2,25 milhões", "4,5 milhões", "6,75 milhões", "9 milhões" ] )
plt.yticks(x_pos, idades) 

plt.title("Distribuição da População do sexo masculino segundo os grupos de idade - Brasil - 2010")

plt.ylabel("Idades")
plt.xlabel("População")

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()