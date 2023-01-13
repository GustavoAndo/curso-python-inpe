def get_year(a):
    if len(a) == 45:
        return a[9:13]
    return None

a = input("Digite o nome do arquivo: ")
# MOD09A1.A2006001.h08v05.005.2006012234657.hdf
y = get_year(a)
print(y)