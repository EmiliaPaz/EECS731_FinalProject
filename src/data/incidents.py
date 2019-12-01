
import pandas as pd 
import numpy as np

df = pd.read_csv('incidents.csv')

df.rename(columns={'IncidntNum':'IncidentNum',
                   'Descript':'Description'},
          inplace=True)

df = df.apply(lambda x: x.astype(str).str.lower())

df['Date'] = pd.to_datetime(df['Date'], format="%m/%d/%Y" )
df['Time'] = pd.to_datetime(df['Time'], format="%H:%M" ).dt.time

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

empty_sample = df[df.isnull().any(axis=1)]
df.dropna(inplace=True)

df.to_csv('../../data/processed/incidents.csv')