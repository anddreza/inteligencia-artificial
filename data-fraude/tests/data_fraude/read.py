import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

contagem_agrupada_female = (
	(df['Sex'] == 'Female') &
	(df['Age'] > 20) &
	(df['Age'] < 50) 
)

numero_de_registros = df[contagem_agrupada_female].shape[0]
print(f"Quantidade por female entre 20 e 40 anos: {numero_de_registros}")

print('-------------------------------------')

contagem_agrupada_male = (
	(df['Sex'] == 'Male') &
	(df['Age'] > 20) &
	(df['Age'] < 40) 

)

numero_de_registros = df[contagem_agrupada_male].shape[0]
print(f"Quantidade por male entre 20 e 40 anos: {numero_de_registros}")
print('-------------------------------------')



contagem_veiculo = df['VehicleCategory'].value_counts()
print(f'Contagem por categoria de carro', contagem_veiculo)
print('-------------------------------------')

contagem_veiculos_envolvidos = df['NumberOfCars'].value_counts()
#contagem_veiculos_envolvidos_com_testemunha = df.groupby('NumberOfCars')['WitnessPresent'].value_counts()
print('Contagem de veiculos envolvidos', contagem_veiculos_envolvidos)
print('-------------------------------------')

# filtro = df['WitnessPresent'] == 'Yes'
# quantidade_de_carros = df[filtro]['NumberOfCars'].sum()
