import pandas as pd


# import csv

dados = pd.read_csv('fraud.csv').head()
print(f'Aqui o head: ')
dados.head()
print(f'Aqui o Data Frame: ')
df = pd.DataFrame(dados)
print(dados)
print(f'Aqui os info: ')
print(dados.info())

print(f'Aqui se ele conseguirá verificar mais de 30 e menos de 40: ')
serie_booleana = (df['Age'] > 30) & (df['Age'] < 40)
print(f'Verificar com mais detalhes', serie_booleana)

serie_gender = df['Sex'] == 'Male' 
