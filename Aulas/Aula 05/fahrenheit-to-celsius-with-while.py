t_min = 0     # temperatura mínima
t_max = 300   # temperatra máxima
delta_t = 20  # delta de temperatura a cada passo
 
fahr = t_min  # temperatura Fahrenheit inicial
 
while fahr <= t_max:
    celsius = 5 * (fahr - 32) / 9
 
    print(fahr, celsius)
 
    fahr = fahr + delta_t