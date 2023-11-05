import pandas as pd

# Cargar el archivo CSV original
input_csv = "moviesn.csv"
df = pd.read_csv('data/moviesn.csv')

# Dividir los géneros en una lista (separados por '|')
df['genres'] = df['genres'].str.split('|')

# Crear una lista con todos los géneros
all_genres = [genre for genres_list in df['genres'] for genre in genres_list]

# Contar la frecuencia de cada género
genre_counts = pd.Series(all_genres).value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']

# Guardar el resultado en un nuevo archivo CSV
output_csv = "genre_counts.csv"  # Nombre del archivo de salida
genre_counts.to_csv(output_csv, index=False)

print(f"Se ha creado el archivo {output_csv} con el recuento de géneros.")
