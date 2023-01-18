import extrair_dados
import matplotlib.pyplot as plt

populacao_masc = [int(x[2]) for x in extrair_dados.dados()]
idades = [x[0] for x in extrair_dados.dados()]

x_pos = [ x for x in range( len(idades) ) ]

plt.bar(x_pos, populacao_masc, align='center',
        color='orange', linewidth=2, edgecolor='black')

plt.yticks([ 0, 2250000, 4500000, 6750000, 9000000 ],
           [ "0", "2,25 milhões", "4,5 milhões", "6,75 milhões", "9 milhões" ] )
plt.xticks(x_pos, idades, rotation=60, fontsize=7) 

plt.title("Distribuição da População do sexo feminino segundo os grupos de idade - Brasil - 2010")

plt.xlabel("Idades")
plt.ylabel("População")

plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.show()