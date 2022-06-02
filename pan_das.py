from numpy import int8
import pandas as pd
diccionario = {
    'Ene': 24,
    'Feb': 28,
    'Mar': 29,
    'Abr': 30,
    'May': 30    
}
print(diccionario)
serie1 = pd.Series(diccionario)
print(serie1)
lista1 = [24,28,29,30,130]
serie2 = pd.Series(lista1, index = ['Ene','Feb','Mar','Mar','Abr'],dtype=int8)
print(serie2)
print(serie2[0])
print(serie2.loc['Mar'])
print(serie2.iloc[2])
print(serie1[3])