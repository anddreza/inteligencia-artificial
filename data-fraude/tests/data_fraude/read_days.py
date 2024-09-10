# import pandas as pd

# dados = pd.read_csv('fraud.csv')
# df = pd.DataFrame(dados)

# filtro = (
# 	  (df['DayOfWeek'] == '') &
# 	  (df['DayOfWeekClaimed'] == '')
# 	)
# quantida = df[filtro].shape[0]
# print(f"Quantidade de registros que se encaixam na categoria entre 30 e 40 anos com carros Sedan e já tiveram outras ocorrências anteriores: {quantida}")