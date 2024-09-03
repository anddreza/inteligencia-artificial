import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

filtro = df['WitnessPresent'] == 'Yes'
# quantidade_de_carros = df[filtro]['NumberOfCars'].sum()
# print(f"Quantidade total de carros envolvidos em acidentes com testemunhas presentes: {quantidade_de_carros}")

numero_de_acidentes = df[filtro].shape[0]
print(f"Número de acidentes com testemunhas presentes: {numero_de_acidentes}")
print('-------------------------------------')

filtro_sex_male_veiculo_mais_caro_com_testemunha = (
	(df['Sex'] == 'Male') &
	(df['Age'] > 20) &
	(df['Age'] < 50) & 
	#(df['VehiclePrice'] == 'more than 69000') &
	(df['VehicleCategory'] == 'Sedan') &
	(df['WitnessPresent'] == 'Yes')
)

numero_de_registros = df[filtro_sex_male_veiculo_mais_caro_com_testemunha].shape[0]
print(f"Número de acidentes com testemunhas presentes com homens entre 20 e 50 anos e com veiculos caros: {numero_de_registros}")