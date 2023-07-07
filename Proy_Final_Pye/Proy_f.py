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

# Gráficamos el histograma por rangos de edad
# for i in range(0,Rangos.__len__()):

#     salaries_by_age = df[(df['Salario'] != 0) & (df['Edad'] >= Rangos[i]) ]

#     if i < Rangos.__len__() - 1:
#         salaries_by_age = salaries_by_age[salaries_by_age['Edad'] < Rangos[i+1]]
    
#     salaries_list = salaries_by_age['Salario'].tolist()
    
#     # Create the histogram
#     plt.hist(salaries_list)

#     # Add labels and title
#     if i == Rangos.__len__() - 1: 
#         plt.title(f"Salary Histogram for ages {Rangos[i]} +")
#     else:
#         plt.title(f"Salary Histogram for ages {Rangos[i]} - {Rangos[i+1] - 1}")

#     plt.xlabel("Salary")
#     plt.ylabel('Frequency')

#     # Display the histogram
#     plt.show()

#     # HACER BOXPLOT
#     plt.boxplot(salaries_list)
#     # Add labels and title
#     if i == Rangos.__len__() - 1: 
#         plt.title(f"BoxPlot for ages {Rangos[i]} +")
#     else:
#         plt.title(f"BoxPlot for ages {Rangos[i]} - {Rangos[i+1] - 1}")
#     # show plot
#     plt.show()

salaries_range1 = df[(df['Salario'] != 0) & (df['Salario'] <= 50000)]
salaries_range2 = df[(df['Salario'] != 0) & (df['Salario'] > 50000) & (df['Salario'] <= 100000)]
salaries_range3 = df[(df['Salario'] != 0) & (df['Salario'] > 10000) & (df['Salario'] <= 150000)]
salaries_range4 = df[(df['Salario'] != 0) & (df['Salario'] > 150000)]

# Create the histogram
plt.hist(salaries_range1)

plt.title(f"Salary Histogram for ages {salaries_range1} +")
plt.xlabel("Salary")
plt.ylabel('Frequency')

plt.show()

plt.hist(salaries_range2)

plt.title(f"Salary Histogram for ages {salaries_range2} +")
plt.xlabel("Salary")
plt.ylabel('Frequency')

plt.show()

plt.hist(salaries_range3)

plt.title(f"Salary Histogram for ages {salaries_range3} +")
plt.xlabel("Salary")
plt.ylabel('Frequency')

plt.show()

plt.hist(salaries_range4)

plt.title(f"Salary Histogram for ages {salaries_range4} +")
plt.xlabel("Salary")
plt.ylabel('Frequency')

plt.show()



# # # Mediana
# # print(f"Mediana: {salaries_by_age['Salario'].median()}")

# # # Media
# # print(f"Media: {salaries_by_age['Salario'].mean()}")

# # # Moda  
# # print(f"Moda: {salaries_by_age['Salario'].mode()}")

# # # Minimo
# # print(f"Minimo: {salaries_by_age['Salario'].min()}")

# # # Maximo
# # print(f"Maximo: {salaries_by_age['Salario'].max()}")

# # # Cuartiles
# # print(f"Cuartiles: {salaries_by_age['Salario'].quantile([0.25,0.5,0.75])}")







# salario_femenino = salaries[salaries['Sexo'] == 2]

# salario_masculino = salaries[salaries['Sexo'] == 1]

# plt.boxplot([salary < 500000 for salary in salario_femenino['Salario'].tolist()], whis=350)
# # whis = 350

# plt.show()
