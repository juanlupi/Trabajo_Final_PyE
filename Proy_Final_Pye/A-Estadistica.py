import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('ECH_2022 - BD Proyecto Final PyE 2023.csv')

#Punto A
#Parte 1 a)
poblacion_economica_activa = df[df['PEA'] != 0]
poblacion_desempleada = poblacion_economica_activa[poblacion_economica_activa['Desempleo'] != 0]
tasa_de_desempleo = poblacion_desempleada['ID'].count() / poblacion_economica_activa['ID'].count()

print (f"Tasa de desempleo {tasa_de_desempleo} ")

#############################################################################################################
# b)
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

#############################################################################################################
#Parte 2 a)
#Seteamos un limite de $150000 en el monto del salario para que los datos sean mas legible
Corte = 150000
salaries = df[(df['Salario'] != 0) & (df['Salario'] < Corte)]

#Pasamos los datos a una lista para poder graficarlos
salaries_list = salaries['Salario'].tolist()

# Create the histogram
plt.hist(salaries_list)

# Add labels and title
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Histogram')

# Display the histogram
plt.show()

#############################################################################################################
# b)
# HACER BOXPLOT
plt.boxplot(salaries_list)

plt.title('Salaries Boxplot')

# show plot
plt.show()

#############################################################################################################
# c)
salaries_all = df[(df['Salario'] != 0)]
# Mediana
print(f"Mediana: {salaries_all['Salario'].median()}")

# Media
print(f"Media: {salaries_all['Salario'].mean()}")

# Moda  
print(f"Moda: {salaries_all['Salario'].mode()}")

##############################################################################################################  
# d)
# Minimo
print(f"Minimo: {salaries_all['Salario'].min()}")

# Maximo
print(f"Maximo: {salaries_all['Salario'].max()}")

# Cuartiles
print(f"Cuartiles: {salaries_all['Salario'].quantile([0.25,0.5,0.75])}")

##############################################################################################################
# e)
Corte = 70000 # Seteamos un limite de $70000 en el monto del salario para que los datos sean mas legibles
salario_femenino = salaries[(salaries['Sexo'] == 2) & (salaries['Salario'] < Corte)]

salario_masculino = salaries[(salaries['Sexo'] == 1) & (salaries['Salario'] < Corte)]

plt.boxplot(salario_masculino['Salario'].tolist()) # whis = 350
plt.title('BoxPLot Salario Masculino')
plt.show()

plt.boxplot(salario_femenino['Salario'].tolist())
plt.title('BoxPLot Salario Femenino')
plt.show()

salario_Montevideo = salaries[(salaries['region'] == 1) & (salaries['Salario'] < Corte)]

salario_Interior = salaries[(salaries['region'] != 1) & (salaries['Salario'] < Corte)]

plt.boxplot(salario_Interior['Salario'].tolist()) # whis = 350
plt.title('BoxPLot Salario Interior')
plt.show()

plt.boxplot(salario_Montevideo['Salario'].tolist())
plt.title('BoxPLot Salario Montevideo')
plt.show()









