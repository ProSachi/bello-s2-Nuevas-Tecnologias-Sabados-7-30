import pandas as pd

datos_empleados = { 'id': [1, 2, 3, 4, 5], 
                   'nombre': ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro'], 
                   'departamento': ['Ventas', 'IT', 'Vnts', 'Tecnologia', 'Ventas'] 
                   }

#Convertimos a dataframe
df_empleados = pd.DataFrame(datos_empleados)

#Definimos nuestra lista estricta
deptos_oficiales = ['Ventas', 'Tecnologia']

# Usamos ~ (NOT) para buscar a los que violan la regla de la lista 
mascara_infractores = ~df_empleados['departamento'].isin(deptos_oficiales) 

# Filtramos el DataFrame usando la máscara para ver los errores 
errores_detectados = df_empleados[mascara_infractores]

#Hacemos un print de los datos que no cumplen nuestra lista
print(errores_detectados) 

#Hacemos un diccionario para aplicar una traducción
traduccion = { 'IT': 'Tecnologia', 'Vnts': 'Ventas' }

# Aplicamos la traducción solo a la columna afectada 
df_empleados['departamento'] = df_empleados['departamento'].replace(traduccion)

