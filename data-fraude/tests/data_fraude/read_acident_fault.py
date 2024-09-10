import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

# Acidentes urbanos e rurais 
# com seguro e sem seguro
# e com a quantidade de veiculos envolvidos 


contagem_agrupada_urban_policy_holder_com_mais_de_um_veiculo = (
	(df['AccidentArea'] == 'Urban') &
	(df['Fault'] == 'Policy Holder') &
	(df['NumberOfCars'] != '1 vehicle') &
	(df['FraudFound_P'] != '0')
)

numero = df[contagem_agrupada_urban_policy_holder_com_mais_de_um_veiculo].shape[0]
print('Contagem na cidade, com seguro e com mais de um carro', numero)

print('-------------------------------------')

contagem_agrupada_urban_policy_holder_com_um_veiculo = (
	(df['AccidentArea'] == 'Urban') &
	(df['Fault'] == 'Policy Holder') &
	(df['NumberOfCars'] == '1 vehicle') &
	(df['FraudFound_P'] != '0')
)


numeros = df[contagem_agrupada_urban_policy_holder_com_um_veiculo].shape[0]
print('Contagem na cidade, com seguro e com um carro', numeros)
print('-------------------------------------')