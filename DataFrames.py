# Importamos la librería pandas para trabajar con DataFrames
import pandas as pd

# Leemos el archivo CSV y lo cargamos en un DataFrame
df = pd.read_csv("./kodland_data.csv")  # './kodland_data.csv' es el archivo que contiene los datos
df  # Visualizamos el contenido del DataFrame

# *** TABLA 1: OPERACIONES BÁSICAS ***
# Calculamos el valor máximo de la columna 'points'
df.points.max()  # Devuelve el valor máximo de los puntos

# Calculamos el valor mínimo de la columna 'points'
df.points.min()  # Devuelve el valor mínimo de los puntos

# Sumamos todos los valores de la columna 'points'
df.points.sum()  # Devuelve la suma total de los puntos

# *** TABLA 2: FILTRADO DE DATOS ***
# Filtramos las filas donde los puntos sean iguales al valor máximo
df[df.points == df.points.max()]  # Devuelve las filas con el puntaje máximo

# Filtramos las filas donde los puntos sean iguales al valor mínimo, mostrando columnas específicas
df[df.points == df.points.min()][['id', 'course', 'points']]  
# Devuelve las filas con el puntaje mínimo y solo muestra 'id', 'course' y 'points'

# *** TABLA 3: FILTRO Y OPERACIONES POR CATEGORÍA ***
# Filtramos las filas donde la columna 'course' sea igual a 'Python Pro'
filtered_df = df[df.course == 'Python Pro']

# Calculamos el total de puntos de las filas filtradas
total_points = filtered_df.points.sum()  # Suma total de los puntos para 'Python Pro'
print(total_points)  # Imprimimos el resultado

# Mostramos los primeros 5 registros del DataFrame
print(df.head())  # Muestra las primeras 5 filas del DataFrame

# *** TABLA 4: VALORES ÚNICOS ***
# Calculamos la cantidad de valores únicos en la columna 'course'
unique_courses = df.course.nunique()  # Devuelve el número de cursos únicos
print(f"Número de cursos únicos: {unique_courses}")

# *** TABLA 5: ESTADÍSTICAS ***
# Calculamos el promedio de los puntos
average_points = df.points.mean()  # Devuelve el promedio de la columna 'points'
print(f"Promedio de puntos: {average_points}")

# Calculamos la varianza de los puntos
variance_points = df.points.var()  # Devuelve la varianza de la columna 'points'
print(f"Varianza de puntos: {variance_points}")

# Calculamos la desviación estándar de los puntos
std_dev_points = df.points.std()  # Devuelve la desviación estándar de los puntos
print(f"Desviación estándar de puntos: {std_dev_points}")

# *** TABLA 6: LIMPIEZA DE DATOS ***
# Verificamos cuántos valores no nulos tiene la columna 'points'
not_null_points = df.points.notna().sum()  # Devuelve el número de valores no nulos
print(f"Valores no nulos en 'points': {not_null_points}")

# Verificamos si todos los valores de 'points' son mayores a 0
all_positive = (df.points > 0).all()  # Devuelve True si todos los valores son mayores a 0
print(f"Todos los puntos son mayores a 0: {all_positive}")

# *** GUARDAMOS RESULTADOS ***
# Guardamos los datos procesados en un archivo CSV para futuras referencias
df.to_csv("processed_kodland_data.csv", index=False)  # Se guarda el DataFrame en un nuevo archivo CSV

#Estos son algunos ejemplos de comandos de pandas con DataFrames
