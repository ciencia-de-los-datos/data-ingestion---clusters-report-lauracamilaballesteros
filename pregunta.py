"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


import re

#Sustituir los espacios en blanco en uno solo .
def sustituir_espacio(texto):
  pattern = re.compile(r'\s+')
  texto = re.sub(pattern = pattern, repl= ' ',string = texto)
  texto = re.sub(r'\.', repl= '',string = texto)
  return texto

#Funcion para limpiar los datos de porcentaje
def sustituir_porcentaje(texto):
  pattern = re.compile(r'(\d+),(\d+)\s%')
  texto = re.sub(pattern=pattern, repl=r'\1.\2', string=texto)
  return texto


def ingest_data():

    #
    # Inserte su código aquí
    #
    
    df = pd.read_fwf("clusters_report.txt", skiprows=4, header = None)
    
    df.columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']
    
    df['principales_palabras_clave']=df.fillna(method='ffill').groupby('cluster')['principales_palabras_clave'].transform(lambda x: ' '.join(x))
    df=df.dropna().reset_index(drop=True)
    
    df['principales_palabras_clave'] = df['principales_palabras_clave'].apply(sustituir_espacio)
    
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].apply(sustituir_porcentaje)

    return df
