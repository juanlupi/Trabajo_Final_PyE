import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('ECH_2022 - BD Proyecto Final PyE 2023.csv')

#Punto A
#Parte 1 a)
poblacion_economica_activa = df[df['PEA'] != 0]
poblacion_desempleada = poblacion_economica_activa[poblacion_economica_activa['Desempleo'] != 0]
tasa_de_desempleo = poblacion_desempleada['ID'].count() / poblacion_economica_activa['ID'].count()

print (f"Tasa de desempleo {tasa_de_desempleo} ")

#Parte 1 b)

# Calculamos la tasa de desempleo por rango de edad
Rangos = [14,18,26,41]
TasasPorRangos = {}

for i in range(0,Rangos.__len__()):
    
    p_e_a = df[(df['PEA'] != 0) & (df['Edad'] >= Rangos[i]) ]

    if i < Rangos.__len__() - 1:
        p_e_a = p_e_a[p_e_a['Edad'] < Rangos[i+1]]

    p_d = p_e_a[p_e_a['Desempleo'] != 0]
    tasa_de_desempleo = p_d['ID'].count() / p_e_a['ID'].count()
    
    if i == Rangos.__len__() - 1: 
        TasasPorRangos[f"{Rangos[i]} +"] = tasa_de_desempleo
    else: 
        TasasPorRangos[f"{Rangos[i]} - {Rangos[i+1] - 1}"] = tasa_de_desempleo

# Graficamos la tasa de desempleo por rango de edad
for i in TasasPorRangos:
    plt.bar(i, TasasPorRangos[i])
    
plt.xlabel('Rango de edad')
plt.ylabel('Tasa de desempleo')
plt.title(f'Tasa de desempleo por rango de edad')
plt.show()


#Parte 2 a)
# Cambiamos la data a un formato que se pueda graficar (lista)
for i in range(0,Rangos.__len__()):
    
    df = df[ (df['Edad'] >= Rangos[i] )]

    if i < Rangos.__len__() - 1:
        df = df[df['Edad'] < Rangos[i+1]]

    salaries = df[df['Salario'] != 0]
    
    salaries_list = salaries['Salario'].tolist()
    
    # Create the histogram
    plt.hist(salaries_list)

    # Add labels and title
    plt.xlabel('Salary Upper')
    plt.ylabel('Frequency')
    plt.title('Salary Histogram')

    # Display the histogram
    plt.show()

    # HACER BOXPLOT
    plt.boxplot(salaries_list)
    
    # show plot
    plt.show()

    # Mediana
    print(f"Mediana: {salaries['Salario'].median()}")

    # Media
    print(f"Media: {salaries['Salario'].mean()}")

    # Moda  
    print(f"Moda: {salaries['Salario'].mode()}")

    # Minimo
    print(f"Minimo: {salaries['Salario'].min()}")

    # Maximo
    print(f"Maximo: {salaries['Salario'].max()}")

    # Cuartiles
    print(f"Cuartiles: {salaries['Salario'].quantile([0.25,0.5,0.75])}")






salario_femenino = salaries[salaries['Sexo'] == 2]

salario_masculino = salaries[salaries['Sexo'] == 1]

plt.boxplot([salary < 500000 for salary in salario_femenino['Salario'].tolist()], whis=350)
# whis = 350

plt.show()
