import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Carga los datos
movies = pd.read_csv('data/movies.csv').head(100)

# Combina título y géneros en una sola columna de características
movies['features'] = movies['title'] + ' ' + movies['genres']

# Vectorización de características usando TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies['features'])

# Cálculo de similitud del coseno
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Selecciona 20 películas aleatorias
random_movies = movies.sample(n=20)

# Simula la selección del usuario de 5 películas
user_selection = random_movies.sample(n=5)['title']

def get_recommendations(movie_title, cosine_sim=cosine_sim):
    # Encuentra el índice de la película que coincide con el título
    idx = movies[movies['title'] == movie_title].index[0]

    # Obtiene las puntuaciones de similitud para todas las películas con respecto a la película seleccionada
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ordena las películas en función de las puntuaciones de similitud
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Obtiene las 10 películas más similares (excluyendo la película seleccionada)
    sim_scores = sim_scores[1:11]

    # Obtiene los índices de las películas recomendadas
    movie_indices = [i[0] for i in sim_scores]

    # Devuelve las películas recomendadas
    return movies['title'].iloc[movie_indices]

# Recomendaciones basadas en las 5 películas seleccionadas por el usuario
recommendations = []
for movie_title in user_selection:
    recommendations.extend(get_recommendations(movie_title))

# Elimina duplicados y las películas ya seleccionadas
recommendations = list(set(recommendations) - set(user_selection))

# Obtiene las 10 películas recomendadas finales
recommended_movies = recommendations[:10]

# Código de la aplicación Flask
from flask import Flask, render_template, request

app = Flask(__name__)

# Las rutas de las vistas de Flask se agregan aquí

@app.route('/')
def index():
    # Inserta aquí el código para obtener las 20 películas aleatorias
    random_movies = movies.sample(n=20)  # Modifica esto según tus necesidades
    return render_template('index.html', random_movies=random_movies)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    selected_movies = request.form.getlist('selected_movies')
    # Inserta aquí el código para generar recomendaciones basadas en las películas seleccionadas
    # Usar la variable recommended_movies
    return render_template('recommendations.html', recommended_movies=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
