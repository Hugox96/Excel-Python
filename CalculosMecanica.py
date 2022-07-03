# -*- coding: utf-8 -*-
"""CalculosMecanica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hg8NfwVA8L9uVl_HX6gi4QNNBl0H54jU
"""

import pandas as pd
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabela de um jeito mais bonito

print('---------------- Calculos da Média ------------------------------')

print("Media de Largura(cm): ", str(round(mean(tabela['L']),2)))
print("Media do Comprimento(cm): ", str(round(mean(tabela['C']),2)))
print("Media da Area(cm²): ", str(round(mean(tabela['Área']),2)))

print('---------------- Calculos do Desvio Padrão Amostral -----------------')

print("Desvio Padrão da Largura(cm): ", str(round(std(tabela['L']),2)))
print("Desvio Padrão da Comprimento(cm): ", str(round(std(tabela['C']),2)))
print("Desvio Padrão da Área(cm²): ", str(round(std(tabela['Área']),2)))


print('---------------- Calculos Erro da Media -----------------')

Raiz_das_medidas = 5

Dp_Largura = np.std(tabela["L"])
Erro_Media_Largura = Dp_Largura / Raiz_das_medidas
print("Erro médio da Largura(cm): ",Erro_Media_Largura)

Dp_Comprimento = np.std(tabela["C"])
Erro_Media_Comprimento = Dp_Comprimento / Raiz_das_medidas
print("Erro médio do Comprimento(cm): ", Erro_Media_Comprimento)


Dp_Area = np.std(tabela["Área"])
Erro_Media_Área = Dp_Area / Raiz_das_medidas
print("Erro médio da Área (cm²): ",Erro_Media_Área)

print('---------------- Calculos Erro Total  -----------------')

Erro_do_instrumento = 0.1

Erro_total_largura = np.sqrt((Erro_do_instrumento)**2 + (Dp_Largura)**2)
print(Erro_total_largura)



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabela = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
#display(tabela) #vamos imprimir a tabelo de um jeito mais bonito


# Criando o histograma para os dados da largura, com o int
plt.hist(tabela['L'], bins= 3, edgecolor="black")

# Colocando o título no histograma
plt.title("Histograma Largura")

média = 74.9
cor = "#FA8072"
plt.axvline(média, color=cor, label="Média_Largura: 149,5")
plt.legend()

plt.grid()

# Colocando legenda nos Eixos
plt.xlabel("Largura (cm)")
plt.ylabel("Frequência dos dados")

plt.tight_layout()
 

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabela = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
#display(tabela) #vamos imprimir a tabelo de um jeito mais bonito


# Criando o histograma para os dados da largura, com o int
plt.hist(tabela['Área'],bins=3, edgecolor="black")

# Colocando o título no histograma
plt.title("Histograma Area (cm)")

média = 11203.23
cor = "#FA8072"
plt.axvline(média, color=cor, label="Média_Área: 11203.23")
plt.legend()

plt.grid()

# Colocando legenda nos Eixos
plt.xlabel("Área (cm²)")
plt.ylabel("Frequência dos dados")

plt.tight_layout()
 

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/PlanilhaMec.xlsx")#aqui irá ler os dados em Excel


plt.scatter(tabela["L"],tabela["C"],) #Aqui posso criar um gráfico de dispersão com os eixos x e y
plt.xlabel("Largura") #Colocando legendas no eixo x
plt.ylabel("Comprimento") #Colocando legendas no eixo y

plt.grid()

plt.show()