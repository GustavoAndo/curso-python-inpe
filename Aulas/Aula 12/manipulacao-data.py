# Importação da biblioteca a ser utilizada
import datetime as dt

# Informacões sobre a biblioteca:
# help(dt)

# retornar um objeto do tipo data com os valores atuais do sistema:
data_atual = dt.date.today()
print(data_atual)
data_atual = dt.datetime.today()
print(data_atual)

print(data_atual.year)
print(data_atual.month)
print(data_atual.day)

# obter qualquer uma destas partes da estrutura de tempo:
# time.struct_time(tm_year=2023, tm_mon=1, tm_mday=13, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=13, tm_isdst=-1)
print(data_atual.timetuple())
# ajuda
help(data_atual.timetuple())
#exemplo de uso:
print(data_atual.timetuple().tm_year)

# definição de uma data em um objeto datetime
print(dt.date(2003,8,2))

# Realizar a diferença entre a data do final do ano com a data do inicio do ano
inicio_ano_anterior = dt.date(2022,1,1)
final_ano_anterior = dt.date(2022,12,31)
print(final_ano_anterior - inicio_ano_anterior)

# Formatação de data para apresentação
print(data_atual.strftime("%d/%m/%Y"))

# Imprime a data atual com formato ano_diaJuliano
data_atual.strftime("%Y_%j")

# Formatação de data e hora para apresentação
print(data_atual.strftime("%d/%m/%Y %H:%M:%"))

# Transformar string em data
nova_data = dt.datetime.strptime('2017/10/24 07:34:18', '%Y/%m/%d %H:%M:%S')
print(nova_data)

# Mostrar um ano anterior a data atual
print(dt.date(data_atual.year -1 , data_atual.month, data_atual.day))
print(data_atual.replace(2023))