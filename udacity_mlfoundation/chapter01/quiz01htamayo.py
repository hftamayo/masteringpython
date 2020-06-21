import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

#mejorar el codigo de las etiquetas
etiquetas = list(df.columns)
for etiqueta in etiquetas:
    etiqueta.replace(' ', '_')
df.columns = etiquetas
df.head()

#mejorar el codigo de las funciones comparativas
