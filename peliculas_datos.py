import random

import pandas as pd

# Script para generar archivo csv
titulos = [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
    "Avatar",
    "Gladiator",
    "The Godfather",
    "Jurassic Park",
    "Back to the Future",
]
generos = [
    "Acción",
    "Ciencia Ficción",
    "Drama",
    "Terror",
    "Aventura",
    "Suspenso",
    "Comedia",
]

peliculas = []

for i in range(1, 301):
    pelicula = {
        "id": i,
        "titulo": random.choice(titulos),
        "anio": random.randint(1990, 2025),
        "genero": random.choice(generos),
        "calificacion": round(random.uniform(1.0, 5.0), 1),
    }
    peliculas.append(pelicula)


df_peliculas = pd.DataFrame(peliculas)
df_peliculas.to_csv("datos.csv", index=False)
