import pandas as pd
import numpy as np
#print(f"Pandas versión: {pd.__version__}")
#print(f"Pandas versión: {np.__version__}")


dfprimero = pd.read_csv("data/sucios/diccionario.csv")

#Analisis inicial del dataframe
#dfprimero.info()

#las n primeras filas
#print(dfprimero.head(2))

#las n primeras filas
#print(dfprimero.tail(2))



edad = (dfprimero["edad"].isna().sum() / len(dfprimero))*100
# 7 nulos cuando representa en porcetaje de la 
#print(edad)
promedio_edad = dfprimero["edad"].mean()
print(promedio_edad)

dfprimero["edad"] = dfprimero["edad"].fillna(promedio_edad).round(0)

edad = dfprimero["edad"].isna().sum()
print(dfprimero)

