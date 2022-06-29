import pandas as pd
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel("/content/drive/MyDrive/Colab Notebooks/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito

print('---------------- Calculos da Média ------------------------------')

print("Media de Largura(cm): ", str(round(mean(tabela['Largura']),2)))
print("Media do Comprimento(cm): ", str(round(mean(tabela['Comprimento']),2)))
print("Media da Area(cm²): ", str(round(mean(tabela['Área']),2)))

print('---------------- Calculos do Desvio Padrão Amostral -----------------')

print("Desvio Padrão da Largura(cm): ", str(round(std(tabela['Largura']),2)))
print("Desvio Padrão da Comprimento(cm): ", str(round(std(tabela['Comprimento']),2)))
print("Desvio Padrão da Área(cm²): ", str(round(std(tabela['Área']),2)))


print('---------------- Calculos do Desvio Padrão Amostral -----------------')

Raiz_das_medidas = 5

Dp_Largura = np.std(tabela["Largura"])
Erro_Media_Largura = Dp_Largura / Raiz_das_medidas
print(Erro_Media_Largura)

Dp_Comprimento = np.std(tabela["Comprimento"])
Erro_Media_Comprimento = Dp_Comprimento / Raiz_das_medidas
print(Erro_Media_Comprimento)


Dp_Area = np.std(tabela["Área"])
Erro_Media_Área = Dp_Area / Raiz_das_medidas
print(Erro_Media_Área)




