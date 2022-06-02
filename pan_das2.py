import pandas as pd
import numpy as np
inventario= {
    'impresoras': ['Hp','Canon','Epson'],
    'Cantidad':[10,34,50]
}
df1 = pd.DataFrame(inventario, index = ['P1','P2','P3'])
print(df1)
print(type(df1))
print(df1.iloc[0])
print(df1.loc['P3'])

# crear un dataframe a partir de un array numpy
arreglo = np.array([[4,5,2],[5,7,8],[7,3,1]])
print(arreglo)
df2 = pd.DataFrame(arreglo, columns= ['María','Juan','Carlos'], index=['Ene','Feb','Mar'])
print(df2)



