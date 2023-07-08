# Se asume que la muestra es representativa del total de la población. Dado que la
# población activa de Uruguay es de 1.757.161. (2). Suponer que el desempleo se distribuye de forma normal.

# 1) Estimar el desempleo del total de la población
# 2) Elabora intervalo de confianza con 95% de certeza para la variable desempleo.

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

df= pd.read_csv('ECH_2022 - BD Proyecto Final PyE 2023.csv')
PEA = 1757161

# 1
# VOlver a obtener la tasa de desempleo
poblacion_economica_activa = df[df['PEA'] != 0]
poblacion_desempleada = poblacion_economica_activa[poblacion_economica_activa['Desempleo'] != 0]
tasa_de_desempleo = poblacion_desempleada['ID'].count() / poblacion_economica_activa['ID'].count()


desempleados = PEA * tasa_de_desempleo

print (f"Desempleados {desempleados} ")


# Calcular el intervalo de confianza
nivel_confianza = 0.95
error_estandar = st.norm.ppf((1 + nivel_confianza) / 2) * ((tasa_de_desempleo * (1 - tasa_de_desempleo)) / PEA)**0.5

s = st.norm.interval(confidence=0.95, loc=desempleados, scale=error_estandar)

print(f"Intervalo de confianza al 95%: {s}")