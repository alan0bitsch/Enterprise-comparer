from pprint import pprint
import requests
import pandas as pd 
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import numpy as np

TablaGGl = pd.read_csv('GOOGLE.csv', usecols = ['Open', 'Close'])
TablaAMZN = pd.read_csv('AMZN.csv', usecols = ['Open', 'Close', 'Date'])

promedioG = (TablaGGl['Open'] + TablaGGl['Close'])/2
promedioA = (TablaAMZN['Open'] + TablaAMZN['Close'])/2
dateint = [n for n in range(len(TablaAMZN['Date']))]
dates = TablaAMZN['Date']




line_1 = LineString(np.column_stack((dateint, promedioG)))
line_2 = LineString(np.column_stack((dateint, promedioA)))
interseccion = line_1.intersection(line_2)
xinter, yinter = [], []
lineinter = []
try:
    for e in interseccion:
        try:
            xinter.append(e.x)
            yinter.append(e.y)
        except:
            lineinter.append(e)
except:
    print('No hay intersecciones')



intersect_data = {'Fecha': ['2012-09-07', '2012-08-31', '2012-09-21', 
'2012-09-21', '2012-09-19', '2012-09-12', 
'2012-09-10', '2012-10-10', '2012-10-16', 
'2012-10-31', '2012-11-26', '2012-11-15', 
'2012-11-23', '2013-01-10', '2012-12-21', 
'2012-12-06', '2012-11-20', '2012-11-23', 
'2012-11-13', '2012-11-23', '2013-01-22', 
'2013-01-29', '2013-03-01', '2013-10-09', 
'2013-09-19'], 
'Precio': [1639.799349999868, 1641.2714911979704, 1654.9533480677974, 
1658.5333253333333, 1659.33654148019, 1660.1971435714286, 
1663.2789864492734, 1691.1344101444708, 1692.4895965279618, 
1693.2417492555512, 1715.8073798239675, 1726.2867563981188, 
1727.1835096531217, 1757.5397873185213, 1759.3383801837954, 
1763.9197837427373, 1773.4310344309101, 1778.5670437795231, 
1783.7651888353419, 1785.222755354201, 1808.9782392092686, 
1814.861357156437, 1817.3870098367393, 2003.8369545590106, 
2005.531183394605]}



def doubled(promedio):
    diff = [0]
    for n, price in enumerate(promedio):
        if n:
            diff.append(price - promedio[n-1])
    return diff
    

doubled(promedioA)



intersect_dataFrame = pd.DataFrame(intersect_data)

intersect_dataFrame.to_excel('Intersecciones de la Bolsa.xlsx', index=False)







plt.figure(figsize=[20, 20])
plt.subplot(2, 2, 1)
plt.plot(dates, promedioG,'r-', label='Google')
plt.plot(dates, promedioA,'b-', label='Amazon')
plt.plot(xinter, yinter, 'g.', label='Interseccion')
plt.plot(lineinter, 'yx', label='Intersexxion')
plt.title(f'Acciones Empresa1 Vs Empresa2')
plt.ylabel('Valor en $')
plt.xlabel('Fecha')
r = []
plt.xticks(r)
plt.legend()

plt.subplot(2, 2, 2)
plt.title(f'Crecimiento Empresa1')
plt.ylabel('Crecimiento Relativo')
plt.xlabel('Fecha')
plt.stem(dates, doubled(promedioA), linefmt='r-', markerfmt='c.')
plt.plot()
plt.xticks(r)

plt.subplot(2, 2, 3)
plt.title(f'Crecimiento Empresa2')
plt.ylabel('Crecimiento Relativo')
plt.xlabel('Fecha')
plt.stem(dates, doubled(promedioG), linefmt='c-', markerfmt='m.')
plt.plot()
plt.xticks(r)

plt.savefig('pruebatest')
plt.show()
