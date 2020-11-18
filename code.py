import requests
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString

def wgetAMZN(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)


def wgetGGL(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)


wgetGGL("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/GOOGLE.csv")
wgetAMZN("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Clase_4_datos/AMZN.csv")









TablaGGL = pd.read_csv('GOOGLE.csv', usecols=['Date', 'Open', 'Close'])
TablaAMZN = pd.read_csv('AMZN.csv', usecols=['Date', 'Open', 'Close'])


plt.figure(figsize=[12, 15], frameon=False)

dateGGL = TablaGGL['Date']
openGGL = TablaGGL['Open']
closeGGL = TablaGGL['Close']

dates = []         #capaz no hace falta pasar los datos de dateGGL dentro de otra lista
dates_clean = []
for i in range(len(dateGGL)):
    dates.append(dateGGL[i])

for element in dates:
    dates_clean.append(element.replace('-', '')) 

#===============================================================================

med_valueGGL = []
for m in range(len(openGGL)):
    med_valueGGL.append((openGGL[m] + closeGGL[m])//2)
plt.plot(dates_clean, med_valueGGL,'r-', label='google')
    

#===============================================================================
dateAMZN = TablaAMZN['Date']
openAMZN = TablaAMZN['Open']
closeAMZN = TablaAMZN['Close']

med_valueAMZN = []
for n in range(len(openAMZN)):
    med_valueAMZN.append((openAMZN[n] + closeAMZN[n])//2)
plt.plot(dates_clean, med_valueAMZN, 'y-', label='amazon')
#===============================================================================





#intersect_data = {
#    'Fecha' : xinter,
#    'Precio' : yinter

#}

#intersect_dataFrame = pd.DataFrame(intersect_data)

#intersect_dataFrame.to_excel('Intersecciones de la Bolsa')

#==================================================================================



#plt.stem(x, y2, label = 'dx')





r = []

plt.ylabel('Dólares')
plt.xlabel('Fecha')
plt.xticks(r)
plt.legend(loc='upper left')
#plt.savefig('Acciones GGL Vs AMZN.png')
plt.show()


