import time


variablex=time.localtime()
datentime=time.strftime("%c",variablex)
print(datentime)

month=datentime[4:7]
print(month)

year=datentime[20:24]
print(year)

hournmix=datentime[11:16]
print(hournmix)



