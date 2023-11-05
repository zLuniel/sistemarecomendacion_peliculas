import pandas as pd
import re

# Cargar el archivo CSV original
input_csv = "movies.csv"
df = pd.read_csv('data/movies.csv')

# Expresión regular para extraer el año del título
year_pattern = r'\((\d{4})\)'  # Busca un patrón de 4 dígitos entre paréntesis

# Función para extraer el año de un título
def extract_year(title):
    match = re.search(year_pattern, title)
    if match:
        return int(match.group(1))
    else:
        return None

# Crear una nueva columna 'year' que contiene el año de lanzamiento
df['year'] = df['title'].apply(extract_year)

# Filtrar películas entre 2018 y 2022 (ajusta el rango según tus necesidades)
filtered_df = df[(df['year'] >= 2017) & (df['year'] <= 2019)]

# Especifica el nombre del archivo CSV de salida
output_csv = "output_filtered.csv"

# Guardar el DataFrame filtrado en un nuevo archivo CSV
filtered_df.to_csv(output_csv, index=False)

print(f"Se han reducido los registros y se ha creado el archivo {output_csv}.")
