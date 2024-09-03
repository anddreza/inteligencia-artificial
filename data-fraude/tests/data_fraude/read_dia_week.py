# Analise Atemporal
import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

# Criando um filtro para identificar registros onde o 'DayOfWeek' e o 'DayOfWeekClaimed' são incoerentes
filtro_incoerente = df['DayOfWeek'] != df['DayOfWeekClaimed']

# Aplicando o filtro para identificar os registros suspeitos
registros_incoerentes = df[filtro_incoerente].shape[0]

print('Criando um filtro para identificar registros onde o DayOfWeek e o DayOfWeekClaimed são incoerentes. Aplicando o filtro para identificar os registros suspeitos', registros_incoerentes)