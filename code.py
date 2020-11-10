import pandas as pd
import numpy as np


ruta = input()       #el usuario especifica las dos empresas que quiere comparar
ruta2= input()
period = input()      #el periodo de tiempo del que sacamos el promedio de los valores y decimos cuanto crecio/decrecio
fecha_ini = input()   #el usuario establece desde que fecha hasta que fecha hacer el periodo
fecha_fin = input()


#aca me hice un lio mental porque hay tomarlo segun la fecha, yo lo estaba pensando mal
Tabla = pd.read_csv(ruta, index_col='Date')
open = Tabla['Open']
close = Tabla['Close']


#esto para despues


dailyvalue = (open + close)/2      

#datos de la segunda empresa

Tabla2 = pd.read_csv(ruta2, index_col='Date')
open2 = Tabla.loc['Open']
close2 = Tabla.loc['Close']
dailyvalue2 = (open2 + close2)/2


