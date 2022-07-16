# -*- coding: utf-8 -*-
"""CalculosMecanica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hg8NfwVA8L9uVl_HX6gi4QNNBl0H54jU
"""

!pip install nbconvert

"""**Para começar a coletar os dados vamos realizar os seguintes cálculos:**

1.   Média de C, L e A
2.   Desvio Padrão de C, L e A
3.   Erro da Média de C, L A
4.   Erro Padrão de C e L

**O erro da média é calculado pela seguinte relação:**

\begin{equation}
 \boxed{σ_{\overline{x}} = \frac{\sigma_{x}}{\sqrt{N}}} 
\end{equation}

**O erro da padrão é calculado pela seguinte relação:**

\begin{equation}
 \boxed{\sigma = \sqrt{\sigma_A^2 + \sigma_B^2}} 
\end{equation}
"""

import pandas as pd
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel("/content/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabela de um jeito mais bonito

print()

print('---------------- Calculos da Média ------------------------------')

print("Media do Comprimento(cm): ", str(round(mean(tabela['C']),2)))
print("Media do Largura(cm): ", str(round(mean(tabela['L']),2)))
print("Media da Área(cm²): ", str(round(mean(tabela['Área']),2)))

print()

print('---------------- Calculos do Desvio Padrão Amostral -----------------')

print("Desvio Padrão da Comprimento(cm): ", str(round(std(tabela['C']),2)))
print("Desvio Padrão da Largura(cm): ", str(round(std(tabela['L']),2)))
print("Desvio Padrão da Área(cm²): ", str(round(std(tabela['Área']),2)))

print()

print('---------------- Calculos Erro da Média -----------------')

Raiz_das_medidas = 5


Dp_Comprimento = np.std(tabela["C"])
Erro_Media_Comprimento = Dp_Comprimento / Raiz_das_medidas
print("Erro médio do Comprimento(cm): ", round(Erro_Media_Comprimento,2))

Dp_Largura = np.std(tabela["L"])
Erro_Media_Largura = Dp_Largura / Raiz_das_medidas
print("Erro médio da Largura(cm): ", round(Erro_Media_Largura,2))


Dp_Area = np.std(tabela["Área"])
Erro_Media_Área = Dp_Area / Raiz_das_medidas
print("Erro médio da Área (cm²): ",round(Erro_Media_Área,2))

print()

print('-------- Calculos Erro Padrão Largura e Comprimento --------')

Erro_do_instrumento = 0.1

Erro_total_comprimento = np.sqrt((Erro_do_instrumento)**2 + (Erro_Media_Comprimento)**2)
print("Erro Padrão Comprimento: ",round(Erro_total_comprimento,3))

Erro_total_largura = np.sqrt(((Erro_do_instrumento)**2 + (Erro_Media_Largura)**2))
print("Erro Padrão Largura: ", round(Erro_total_largura,3))

"""# Histogramas que precisamos:

*   Histograma da Largura (cm)
*   Histograma do Comprimento (cm)
*   Histograma da Área (cm²)


"""

import matplotlib.pyplot as plt
tabela = pd.read_excel("/content/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel

bin_count = int(np.ceil(np.log2(len(tabela['L']))) + 1)

# Criando o histograma para os dados da largura, com o int
plt.hist(tabela['L'], bins= bin_count, edgecolor="black")

# Colocando o título no histograma
plt.title("Histograma Largura (cm)")



#Podemos criar um legenda no gráfico para apontar a média
média = 74.9
cor = "#FA8072"
plt.axvline(média, color=cor, label="Média_Largura: 74,9")
plt.legend()

plt.grid()

# Colocando legenda nos Eixos
plt.xlabel("Largura (cm)")
plt.ylabel("Frequência dos dados")

plt.tight_layout()
#plotando o gráfico
plt.show()
plt.savefig('Largura.png')

import matplotlib.pyplot as plt

tabela = pd.read_excel("/content/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
# Criando o histograma para os dados da Área
plt.hist(tabela['Área'],bins=bin_count, edgecolor="black")

# Colocando o título no histograma
plt.title("Histograma Area (cm²)")

#Podemos criar um legenda no gráfico para apontar a média
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

import matplotlib.pyplot as plt

tabela = pd.read_excel("/content/PlanilhaMec.xlsx") #aqui irá ler os dados em Excel
# Criando o histograma para os dados da Área
plt.hist(tabela['C'],bins=5, edgecolor="black")

# Colocando o título no histograma
plt.title("Histograma Comprimento(cm)")

#Podemos criar um legenda no gráfico para apontar a média
média =  149.5
cor = "#FA8072"
plt.axvline(média, color=cor, label="Média_Comprimento:  149.5") 
plt.legend()

plt.grid()

# Colocando legenda nos Eixos
plt.xlabel("Comprimento(cm)")
plt.ylabel("Frequência dos dados")

plt.tight_layout()
 

plt.show()

"""# Calculando a correlação entre dos dados do comprimento e largura.

**Para isso iremos utilizar a covariancia entre x e y e coeficiente de Pearson (r). Depois iremos criar o gráfico de dispersão para visualizar como as grandezas de correlacionam graficamente.**

**Coeficiente de correlação linear de Pearson(r) que varia o intervalo entre -1 e 1.**


\begin{equation}
 \boxed{r = \frac{\sigma_{xy}}{\sigma_{x}\sigma_{y}}} 
\end{equation}

Pela só precisamos calcular a covariancia e dividir pelo produto dos desvios padraões

"""

import pandas as pd
import numpy as np


print("Calculando a covariancia entre comprimento e largura")
Covariancia = np.cov(tabela["C"], tabela["L"])[1][0]

print()

print("Covariancia entre Comprimento e Largura:", Covariancia)

print()

print("Calculando o Coeficiente de Pearson")

print()

r = Covariancia/(Dp_Comprimento*Dp_Largura)

print("Coeficiente de Pearson (r) =", r)

"""**Podemos ver que tanto a covariancia, quanto o coeficente de Pearson deram valores negativos, logo as grandezas de comprimento e largura não são correlacionadas entre si, na verdade são inversamente correlacionadas. 
Quando uma cresce, outra cai e vice-versa. Podemos avaliar isso pelo gráfica de dispersão abaixo.**
"""

import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel("/content/PlanilhaMec.xlsx")#aqui irá ler os dados em Excel

plt.scatter(tabela["C"],tabela["L"],) #Aqui posso criar um gráfico de dispersão com os eixos x e y
plt.xlabel("Comprimento(cm)") #Colocando legendas no eixo x que é o comprimento neste caso
plt.ylabel("Largura(cm)") #Colocando legendas no eixo y que é a largura neste caso

plt.title("Dispersão entre C(cm) x L(cm)")

plt.grid()

plt.show()

import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel("/content/PlanilhaMec.xlsx")#aqui irá ler os dados em Excel

plt.scatter(tabela["L"],tabela["C"],) #Aqui posso criar um gráfico de dispersão com os eixos x e y
plt.xlabel("Largura(cm)") #Colocando legendas no eixo x que é o comprimento neste caso
plt.ylabel("Comprimento(cm)") #Colocando legendas no eixo y que é a largura neste caso
plt.title("Dispersão entre C(cm) x L(cm)")
plt.grid()

plt.show()

"""**Podemos ver também que os gráficos não apresentam correlação, o maior valor de uma grandeza é o menor de outra**

**Agora podemos calcular a incerteza da Área por meio da propagação de erros utilizando a relação abaixo:**

\begin{equation}
 \boxed{σ_{A} = A \sqrt{\left (\dfrac{σ_{c}}{c} \right)^2 + \left (\dfrac{ σ_{l}}{l} \right)^2}} 
\end{equation}
"""

# Calculando as medias de C, L e A

# Média do Comprimento
Media_C = np.mean(tabela["C"])
print("Média de Comprimento: ", round(Media_C,2))

#Média da Largura
Media_L = np.mean(tabela["L"])
print("Média da largura: ", round(Media_L,2))

# A média sendo Média de C * Média de L
A_Media = Media_C * Media_L

print("Média da Área: ", round(A_Media,2))

#Calculando a propagação de erros
Propagação = A_Media * np.sqrt((Erro_do_instrumento/Media_C)**2 + (Erro_do_instrumento/Media_L)**2)
print("Propagação Área: ", round(Propagação,2))

#Erro Padrão da Área 
Erro_Padrao_Area = np.sqrt((Propagação)**2 + (Erro_Media_Área)**2)
print("Erro Padrão da Área: ", round(Erro_Padrao_Area,2))

"""**Calculando compatibilidade em Python**
 
 A compatibilidade  e discrepância é dada pela seguinte relação:

 \begin{equation}
    |\bar{x}-x_{ref}|< 2σ_{\bar{x}}
\end{equation}  

Sendo que se a discrepancia for menor que 2x a incerteza(σx) do valor de referência, aceita-se a compatibilidade.

Caso a discrepância caia na região entre 2x e 3x a incerteza(σx) o experimento é dado como **inconclusivo**.


"""

#Calculando compatibilidade para Área com o valor de referência

#Valor de referencia
Area_ref = 150 * 75
print(Area_ref)
#Valor da Area médio
A_Media 
#Erro medição da Área
Erro_Padrao_Area


# Calculando a discrepancia, vamos precisar calcular o módulo
discrepancia = np.abs(round(A_Media - Area_ref,2)) #Utilizando a função abs para calcular o valor absoluto, ou o módulo
print("O valor da discrepancia é :", discrepancia)

#Agora vamos avaliar a compatibilidade
if(discrepancia < 2*Erro_Padrao_Area):
   print("É compativel com o valor de referencia", discrepancia, "<" , 2*Erro_Padrao_Area)
else:
   print("O valor está na região entre 2x e 3x a incerteza(sigma), logo inconclusivo:", discrepancia, ">",  2*Erro_Padrao_Area)

!jupyter nbconvert --to html CalculosMecanica.ipynb