def in_brazil(modis_name):
    locations = ( "h10v08", "h11v08", "h12v08", "h13v08", "h14v08","h10v09", "h11v09", "h12v09", "h13v09", "h14v09","h10v10", "h11v10", "h12v10", "h13v10", "h14v10", "h12v11", "h13v11", "h14v11", "h12v12", "h13v12")

    if modis_name[17:23] in locations: return True
    return False

a = input("Digite o nome do arquivo: ")
# MOD09A1.A2006001.h08v05.005.2006012234657.hdf
b = in_brazil(a)
print(b)