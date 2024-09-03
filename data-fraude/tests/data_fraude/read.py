import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

contagem_intervalo = df[(df['Age'] > 30) & (df['Age'] < 40)].shape[0]
contagem_agrupada = df.groupby('Sex')['Age'].count()
contagem_veiculo = df['VehicleCategory'].value_counts()

print(f'Contagem por genero', contagem_veiculo)
print('-------------------------------------')
print('A quantidade entre 30 e 40 anos é: ', contagem_intervalo)
print('-------------------------------------')
print(f'Contagem por genero', contagem_agrupada)
print('-------------------------------------')
filtro = (df['Sex'] == 'Male') & (df['Age'] >= 30) & (df['Age'] <= 40) & (df['VehicleCategory'] == 'Sport')
quantidade = df[filtro].shape[0]
print('-------------------------------------')
print(f"Quantidade de registros que se encaixam na categoria: {quantidade}")


contagem_veiculos_envolvidos = df['NumberOfCars'].value_counts()
contagem_veiculos_envolvidos_com_testemunha = df.groupby('NumberOfCars')['WitnessPresent'].value_counts()
print('Contagem de veiculos envolvidos', contagem_veiculos_envolvidos)
print('-------------------------------------')
print('Contagem de veiculos com testemunha presente', contagem_veiculos_envolvidos_com_testemunha)
