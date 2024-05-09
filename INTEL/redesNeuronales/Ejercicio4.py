import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

datos = pd.read_csv("clima - clima.csv")

##################

hay_nulos = datos.isnull().values.any()

if hay_nulos:
    print("El DataFrame tiene valores nulos.")
else:
    print("El DataFrame no tiene valores nulos.")
    
#################    
lista=datos.to_numpy( ).tolist( )
print(lista)    

#################
year = []
temp = []


for i,j in lista:
    year.append(i)
    temp.append(j)

print(year)
print(temp)


mismo_rango = len(year) == len(temp)

if mismo_rango:
    print("Las listas van a la par")
else:
    print("Las listas no van a la par")
    
##############   
    
# Crea un modelo secuencial en Keras.
# Un modelo secuencial es apropiado para una pila simple de capas donde cada capa tiene exactamente un tensor de entrada y un tensor de salida.
# En este caso, el modelo consiste en una sola capa densa (fully connected) con una sola unidad, ya que units=1, y la entrada tiene una sola dimensión (input_shape=[1]).
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Compila el modelo.
# La compilación configura el modelo para el entrenamiento, especificando el optimizador (Nadam en este caso) y la función de pérdida (mean_squared_error).
model.compile(optimizer="Nadam", loss="mean_squared_error")

# Define los datos de entrada (x) y los resultados esperados (y) para el entrenamiento del modelo.
# Convierte las listas en matrices NumPy
x = np.array(year)  # Años como datos de entrada
y = np.array(temp)  # Temperaturas como resultados esperados

# Entrena el modelo con los datos de entrada y resultados esperados.
# epochs=100 especifica el número de veces que se iterará sobre todo el conjunto de datos de entrenamiento durante el entrenamiento.
model.fit(x, y, epochs=1000)

# Guarda el modelo entrenado en un archivo.
# Esto guarda toda la arquitectura del modelo, los pesos y el estado del optimizador.
# Puedes cargar este archivo posteriormente para usar el modelo entrenado sin tener que volver a entrenarlo.
model.save("modeloTemperatura.keras")    


##################


import warnings

# Ignorar todas las advertencias
warnings.filterwarnings("ignore")
#aparecia un mensaje largo que molestaba

#################






# Carga el modelo entrenado desde el archivo "modeloTemperatura.keras"
model = tf.keras.models.load_model("modeloTemperatura.keras")

# Solicita al usuario que ingrese el año para el cual desea predecir la temperatura
valor = float(input("Ingrese el año buscado para predecir su temperatura: "))
#1920-2020

valor_copia = valor

valor = np.array([valor])

# Realiza la predicción utilizando el modelo cargado
prediccion = model.predict([[valor]])  # Envuelve el valor en una lista anidada

# Imprime la predicción
print("La temperatura predicha para el año", valor, "es:", prediccion)



indice_buscado = year.index(valor_copia)

for i in range(len(temp)):
    temeperatura_supuesta = 0
    if i == indice_buscado:
        temperatura_supuesta = temp[i]


print("La temperatura exacta es ",temperatura_supuesta)

print("la cantidad de diferencia(error) es: ",
      abs(prediccion[0][0] - temperatura_supuesta))