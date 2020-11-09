# Enterprise-comparer
Funcionalidad mínima (requisito):
Armar un programa donde se analize la información de ciertas empresas (entrada del usuario) y se las grafique comparativamente.

El usuario debe poder seleccionar empresas de una lista de opciones y el programa debe calcular las intersecciones entre los precios de ambas. Se debe permitir graficar esta información de forma gráfica y almacenar en un archivo de excel las fechas donde ocurrieron las intersecciones.
Se debe permitir graficar la derivada discreta de los valores de bolsa de cada empresa, esto es, la diferencia entre el valor actual y el anterior para cada punto en el tiempo.

El programa debe poder calcular cuál es aquella que creció más y aquella que creció menos en el mes pasado (Octubre), en el mes anterior (Septiembre) y los últimos 12 meses, esta información se debe poder almacenar en un archivo excel.


Gráfico a entregar (requisito):
Realizar un gráfico del valor de las acciones diarias de las compañias Amazon y Google utilizando dos tipos de lineas distintos. El intervalo de fechas que se desea gráficar debe ser seleccionado por el usuario. Encontrar los puntos donde se cruzan los dos gráficos y marcarlos con puntos (para este caso elegir un intervalo donde se produzcan cruces).


Funcionalidad opcional:
El usuario debe poder seleccionar un periodo (1 semana, 1 mes, etc) y fechas de comienzo y de final. El programa debe poder analizar dentro de esas fechas las empresas que crecieron más y menos dentro de cada periodo (1 semana, 1 mes, etc).

El usuario debe poder ingresar una fecha de inicio y de fin, luego el programa analiza para cada empresa aquella que tenga el mayor coeficiente de correlación lineal (aquella que mejor se aproxime a una recta). Pueden utilizar la función scipy.stats.pearsonr de la librería scipy.

Mostrar la pendiente obtenida al aproximar el precio de cada empresa mediante una ecuación lineal, ofrecer la opción de visualizar el precio de cierta empresa superponiendo esta aproximación lineal en el gráfico. Pueden utilizar la función scipy.stats.linregress de la librería scipy.

Para cada gráfico generado el usuario deberá poder ingresar un nombre de archivo y el programa genera un archivo .PNG del gráfico con el nombre indicado.

Crear una aplicación de consola que se ejecute continuamente recibiendo comandos del usuario, el usuario debe indicar el modo de operación que desea y el programa le pide los datos requeridos. Luego de finalizar la tarea el programa regresa al inicio y le pide al usuario el próximo comando. Incluír un comando de ayuda para que el programa indique al usuario cómo utilizarlo. Incluír un comando de salida que provoca la finalización del programa.
