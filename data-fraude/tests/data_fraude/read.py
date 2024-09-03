import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

contagem_intervalo = df[(df['Age'] > 30) & (df['Age'] < 40)].shape[0]
contagem_agrupada = df.groupby('Sex')['Age'].count()

print('A quantidade entre 30 e 40 anos é: ', contagem_intervalo)
print(f'Contagem por genero', contagem_agrupada)

