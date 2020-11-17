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



intervalo_inicio = str(input('Definir inicio (formato yyyy-mm-dd): '))
intervalo_fin = str(input('Definir fin (formato yyyy-mm-dd): '))





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



promedioG = (TablaGGL['Open'] + TablaGGL['Close'])//2
promedioA = (TablaAMZN['Open'] + TablaAMZN['Close'])//2
dateint = [n for n in range(len(TablaAMZN['Date']))]
dates = TablaAMZN['Date']

line_1 = LineString(np.column_stack((dateint, promedioG)))
line_2 = LineString(np.column_stack((dateint, promedioA)))
interseccion = line_1.intersection(line_2)
try:
    xinter = [point.x for point in interseccion]
    yinter = [point.y for point in interseccion]
except TypeError:
    print('No hay intersecciones.')
    xinter, yinter = [], []




#===============================================================================



fechas_analisis = dates[intervalo_inicio::intervalo_fin]

if yinter in fechas_analisis:
    plt.plot(xinter, yinter, 'bo', label='Interseccion')
    
else:
    print('No existe intersección entre los gráficos en el intervalo de fechas seleccionadas')
    

r = []

plt.ylabel('Dólares')
plt.xlabel('Fecha')
plt.xticks(r)
plt.legend(loc='upper left')
plt.savefig('Acciones GGL Vs AMZN.png')
plt.show()




