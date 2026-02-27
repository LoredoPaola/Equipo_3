<<<<<<< HEAD
import random

import pandas as pd

# Script para generar archivo csv
=======

import random
import pandas as pd


>>>>>>> 43ab654 (Agrega script, datos.csv y edita README)
titulos = [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
<<<<<<< HEAD
    "Avatar",
    "Gladiator",
    "The Godfather",
    "Jurassic Park",
    "Back to the Future",
=======
    "Forrest Gump",
    "Gladiator",
    "The Godfather",
    "Jurassic Park",
    "Back to the Future"
>>>>>>> 43ab654 (Agrega script, datos.csv y edita README)
]
generos = [
    "Acción",
    "Ciencia Ficción",
    "Drama",
<<<<<<< HEAD
    "Terror",
    "Aventura",
    "Suspenso",
    "Comedia",
=======
    "Crimen",
    "Aventura",
    "Suspenso",
    "Comedia"
>>>>>>> 43ab654 (Agrega script, datos.csv y edita README)
]

peliculas = []

<<<<<<< HEAD
for i in range(1, 301):
=======
for i in range(1, 601):
>>>>>>> 43ab654 (Agrega script, datos.csv y edita README)
    pelicula = {
        "id": i,
        "titulo": random.choice(titulos),
        "anio": random.randint(1990, 2025),
        "genero": random.choice(generos),
<<<<<<< HEAD
        "calificacion": round(random.uniform(1.0, 5.0), 1),
=======
        "calificacion": round(random.uniform(1.0, 5.0), 1) 
>>>>>>> 43ab654 (Agrega script, datos.csv y edita README)
    }
    peliculas.append(pelicula)


df_peliculas = pd.DataFrame(peliculas)
df_peliculas.to_csv("datos.csv", index=False)
<<<<<<< HEAD
=======
print("Archivo datos.csv generado con éxito con 600 registros.")
>>>>>>> 43ab654 (Agrega script, datos.csv y edita README)
