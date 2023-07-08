import math
import pandas as pd
import scipy.stats as stats

def PruebaUnaCola(tasa_desempleo, referencia, desviacion_estandar, tamaño_muestra):
    z = (tasa_desempleo - referencia) / (desviacion_estandar / math.sqrt(tamaño_muestra))
    valor_critico = 1.645
    if z > valor_critico:
        return "La tasa de desempleo ha aumentado significativamente. Se rechaza la hipótesis nula."
    else:
        return "La tasa de desempleo no ha aumentado significativamente. No se rechaza la hipótesis nula."
    

def PruebaDosColas(salarios_h, salarios_m):
    media_h = sum(salarios_h) / len(salarios_h)
    media_m = sum(salarios_m) / len(salarios_m)
    desviacion_h = stats.tstd(salarios_h)
    desviacion_m = stats.tstd(salarios_m)
    tamaño_muestra_h = len(salarios_h)
    tamaño_muestra_m = len(salarios_m)

    valor_critico = stats.t.ppf(0.995, tamaño_muestra_h + tamaño_muestra_m - 2)

    numerador = media_h - media_m
    denominador = math.sqrt((desviacion_h**2 / tamaño_muestra_h) + (desviacion_m**2 / tamaño_muestra_m))
    t = numerador / denominador

    if abs(t) > valor_critico:
        return "Hay evidencia para afirmar la existencia de diferencias en el salario promedio entre géneros. Se rechaza la hipótesis nula."
    else:
        return "No hay evidencia suficiente para afirmar la existencia de diferencias en el salario promedio entre géneros. No se rechaza la hipótesis nula."


df= pd.read_csv('ECH_2022 - BD Proyecto Final PyE 2023.csv')
poblacion_economica_activa = df[df['PEA'] != 0]
poblacion_desempleada = poblacion_economica_activa[poblacion_economica_activa['Desempleo'] != 0]
tasa_de_desempleo = poblacion_desempleada['ID'].count() / poblacion_economica_activa['ID'].count()

# Parte 1
salario = df[df['Salario'] != 0]
salarios_list = salario['Salario'].tolist()
print("Prueba de una cola")
print(PruebaUnaCola(tasa_de_desempleo, 0.07, stats.tstd(salarios_list), salarios_list.__len__()))

# Parte 2
salario_femenino = df[df['Sexo'] == 2]
salario_femenino_list = salario_femenino['Salario'].tolist()

salario_masculino = df[df['Sexo'] == 1]
salario_masculino_list = salario_masculino['Salario'].tolist()
print("\nPrueba de dos colas")
print(PruebaDosColas(salario_masculino_list, salario_femenino_list))
