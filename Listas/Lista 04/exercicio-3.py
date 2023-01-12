# "Gilberto" -> "++Gilberto++"
print("Gilberto".center(12, "+"))

# "sensoriamento remoto" -> "Sensoriamento remoto" 
print("sensoriamento remoto".capitalize())

# "sensoriamento remoto" -> "Sensoriamento Remoto" 
print("sensoriamento remoto".title())

# "GilberTo" -> "gilberto" 
print("GilberTo".lower())

# "Gilberto" -> "Gilberto**" 
print("Gilberto".ljust(10, "*"))

# "Gilberto" -> "**Gilberto" 
print("Gilberto".rjust(10, "*"))

# " Gilberto" -> "Gilberto" 
print(" Gilberto".lstrip())

# "ser347@dpi.inpe.br" -> ("ser347", "@", "dpi.inpe.br") 
print("ser347@dpi.inpe.br".partition("@"))

# "CBERS_4_PAN5M_20180308" -> ['CBERS', '4', 'PAN5M', '20180308'] 
print("CBERS_4_PAN5M_20180308".split("_"))

# "Gilberto@@@" -> "Gilberto" 
print("Gilberto@@@".rstrip("@"))

# "@@Gilberto@@@" -> "Gilberto" 
print("@@Gilberto@@@".strip("@"))