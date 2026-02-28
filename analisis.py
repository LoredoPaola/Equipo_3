# --- YARG - 27/02/26 - Analisis de los datos, se muestra el numero total de peliculas y un grafico referente al archivo csv ---
import matplotlib.pyplot as plt
import pandas as pd

# --- Carga del archivo csv ---
df_peliculas = pd.read_csv("datos.csv")
print(f"Numero total de peliculas: {len(df_peliculas)}")

# --- Análisis 1: Promedio de calificación por género de película ---
calificacion_genero = df_peliculas.groupby("genero")["calificacion"].mean()

# --- Gráfico 1: Calificación promedio por género ---
plt.figure(figsize=(12, 6))
calificacion_genero.plot(kind="bar", color="#FF9770")
plt.title("Calificación promedio por género de película")
plt.xlabel("Género")
plt.ylabel("Promedio de calificación")
plt.grid(False)
plt.show()
