import pandas as pd

df= pd.read_csv('ECH_2022 - BD Proyecto Final PyE 2023.csv')

#Punto A
#Parte1
poblacion_economica_activa = df[df['PEA'] != 0]
poblacion_desempleada = poblacion_economica_activa[poblacion_economica_activa['Desempleo'] != 0]
tasa_de_desempleo = poblacion_desempleada['ID'].count() / poblacion_economica_activa['ID'].count()

print ('Tasa de desempleo' + tasa_de_desempleo)

#Parte2

Rangos = [14,18,26,41]
TasasPorRangos = {}

for i in range(0,Rangos.count):
    p_e_a = df[(df['PEA'] != 0) & (df['Edad'] >= Rangos[i]) ]
    if i < Rangos.count:
        p_e_a = p_e_a['Edad'] < Rangos[i+1]
        
    p_d = p_e_a[p_e_a['Desempleo'] != 0]
    tasa_de_desempleo = p_d['ID'].count() / p_e_a['ID'].count()
    TasasPorRangos[Rangos[i]] = tasa_de_desempleo

