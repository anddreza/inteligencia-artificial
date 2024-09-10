# Analise Atemporal
import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

# Criando um filtro para identificar registros onde o 'DayOfWeek' e o 'DayOfWeekClaimed' são incoerentes
filtro_incoerente = (
		(df['DayOfWeek'] != df['DayOfWeekClaimed']) &
		(df['FraudFound_P'] != '0') &
		(df['Month'] == 'Jan')
	)

numero_de_registros = df[filtro_incoerente].shape[0]
print(f"Numero de dias entre o dia que reclamou e o dia do acidente verificando se é fraude pelo menos de Janeiro: {numero_de_registros}")

#FraudFound_P
#fraud_found = df['FraudFound_P'] != 0
registros_incoerentes = df[filtro_incoerente].shape[0]


# Aplicando o filtro para identificar os registros suspeitos
registros_incoerentes = df[filtro_incoerente].shape[0]

#print('Criando um filtro para identificar registros onde o DayOfWeek e o DayOfWeekClaimed são incoerentes. Aplicando o filtro para identificar os registros suspeitos', registros_incoerentes)