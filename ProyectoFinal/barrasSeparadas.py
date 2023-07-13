# %%
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

path = "profesiones.xlsx"
dataframe = pd.read_excel(path, nrows=20)

fig = plt.figure(figsize=(15,15))
rubros = dataframe['Profesiones'].tolist()
salario_hombres = dataframe['Hombres'].tolist()
salario_mujeres = dataframe['Mujeres'].tolist()

# Configuración del gráfico
bar_width = 0.35
index = range(len(rubros))

# Crear el gráfico de barras
plt.bar(index, salario_hombres, bar_width, label='Hombres')
plt.bar([i + bar_width for i in index], salario_mujeres, bar_width, label='Mujeres', alpha=0.5)

# Etiquetas, título y leyenda
plt.xlabel('Profesiones')
plt.ylabel('Salarios en pesos')
plt.title('Diferencia salarial entre mujeres y hombres y entre profesiones durante septiembre de 2019')
plt.xticks([i + bar_width/2 for i in index], rubros, rotation=50, ha="right")
plt.legend()

# Mostrar el gráfico
plt.tight_layout()
plt.show()
# %%
