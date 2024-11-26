# Importar las librerías necesarias
from bs4 import BeautifulSoup  # Para analizar el contenido HTML
import requests  # Para hacer solicitudes HTTP y obtener el contenido de las páginas
import pandas as pd  # Para manejar y estructurar datos en un DataFrame
from ast import Continue  # Aunque se importa aquí, no se utiliza en este código
# Crear un diccionario para almacenar los datos de las noticias
# Cada clave será una columna en el DataFrame final
dict_news_03 = {
    "titulos_noticias": [],  # Lista para los títulos de las noticias
    "enlaces": [],           # Lista para los enlaces de las noticias
    "comentarios": [],       # Lista para el número de comentarios
    "fecha_publicacion": [], # Lista para las fechas de publicación
    "tag": []                # Lista opcional para la etiqueta o categoría de la noticia
}

# Definir la URL base de Xataka y las páginas de interés (categorías)
url = "https://www.xataka.com/"
pages = ["ciencia-y-tecnologia", "elon-musk", "google", "nasa", "videojuegos"]

# Recorrer cada página de interés (categoría) para extraer datos
for i in pages:
    # Hacer una solicitud GET para obtener el contenido de la página
    response = requests.get(url + "tag/" + i)
    # Analizar el contenido HTML con BeautifulSoup y el parser lxml
    bs = BeautifulSoup(response.text, "lxml")
    # Buscar todos los artículos que correspondan a las noticias recientes
    temp = bs.find_all('article', "recent-abstract abstract-article")
    
    # Recorrer cada artículo encontrado para extraer su información
    for post in temp:
        # Extraer el enlace de la noticia
        dict_news_03["enlaces"].append(post.h2.a.get("href"))
        # Extraer el título de la noticia
        dict_news_03["titulos_noticias"].append(post.h2.a.text)
        # Extraer el número de comentarios
        dict_news_03["comentarios"].append(post.span.text)
        # Extraer la fecha de publicación (solo los primeros 10 caracteres)
        dict_news_03["fecha_publicacion"].append(post.time.get("datetime")[0:10])
        # Agregar la etiqueta o categoría correspondiente
        dict_news_03["tag"].append(i)

# Crear un DataFrame con los datos extraídos y organizar las columnas
df_news_03 = pd.DataFrame(
    dict_news_03, 
    columns=["titulos_noticias", "enlaces", "comentarios", "fecha_publicacion", "tag"]
)

# Guardar el DataFrame en un archivo CSV para conservar los datos
df_news_03.to_csv("./saved_data.csv", index=False)  # El índice no será incluido en el CSV

# Mostrar el contenido del DataFrame como salida
df_news_03
