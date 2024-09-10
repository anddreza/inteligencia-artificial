import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

#Políticas Específicas: Veículos caros com várias reclamações anteriores (VehiclePrice > X e PastNumberOfClaims > Y) podem levantar suspeitas.
#Ações Tomadas: Falta de testemunhas ou relatórios policiais quando seria esperado.

red_flags = (
	 (df['VehiclePrice'].isin(['more than 69000', '20000 to 29000', '30000 to 39000', 'less than 20000', '40000 to 59000'])) & 
	(df['PastNumberOfClaims'] != '2 to 4') & 
	(df['WitnessPresent'] == 'No') & 
	(df['FraudFound_P'] != '0')
	)

filtro = df[red_flags].shape[0]
print('-------------------------------------')

print(filtro)
