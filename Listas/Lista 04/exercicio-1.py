a = input("Digite o nome do arquivo: ").split(".")

product = a[0]
if product[0:3] == "MOD":
  satellite = "Terra"
else:
  satellite = "unknown"
year_aq = a[1][1:5]
day_aq = a[1][5:]
horizon = a[2][1:3]
vertical = a[2][4:]
collection = a[3]
year_prod = a[4][0:4]
day_prod = a[4][4:7]
hour_prod = a[4][7:9]
min_prod = a[4][9:11]
sec_prod = a[4][11:]
data_format = a[5]

print(""" 
    Satellite...............: {}
    Product.................: {}
    Year of Acquisition.....: {}
    Julian Day..............: {}
    Horizontal Tile.........: {}
    Vertical Tile...........: {}
    Collection..............: {}
    Year of Production......: {}
    Julian Day of Production: {}
    Production Hour.........: {}
    Production Minute.......: {}
    Production Second.......: {}
    Data Format.............: {}
""".format(satellite, product, year_aq, day_aq, horizon, vertical, collection, year_prod, day_prod, hour_prod, min_prod, sec_prod, data_format))

