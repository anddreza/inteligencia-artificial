import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)


# Contagem de acidentes em cada faixa etária
contagem_10_20 = df[(df['Age'] >= 10) & (df['Age'] < 20)].shape[0]
contagem_20_30 = df[(df['Age'] >= 20) & (df['Age'] < 30)].shape[0]
contagem_30_40 = df[(df['Age'] >= 30) & (df['Age'] < 40)].shape[0]
contagem_40_50 = df[(df['Age'] >= 40) & (df['Age'] < 50)].shape[0]
contagem_50_60 = df[(df['Age'] >= 50) & (df['Age'] < 60)].shape[0]
contagem_60_70 = df[(df['Age'] >= 60) & (df['Age'] < 70)].shape[0]
contagem_70_80 = df[(df['Age'] >= 70) & (df['Age'] < 80)].shape[0]
contagem_80_90 = df[(df['Age'] >= 80) & (df['Age'] < 90)].shape[0]
contagem_90_100 = df[(df['Age'] >= 90) & (df['Age'] < 100)].shape[0]

# Exibindo as contagens
print(f"Contagem de 10 a 20 anos: {contagem_10_20}")
print(f"Contagem de 20 a 30 anos: {contagem_20_30}")
print(f"Contagem de 30 a 40 anos: {contagem_30_40}")
print(f"Contagem de 40 a 50 anos: {contagem_40_50}")
print(f"Contagem de 50 a 60 anos: {contagem_50_60}")
print(f"Contagem de 60 a 70 anos: {contagem_60_70}")
print(f"Contagem de 70 a 80 anos: {contagem_70_80}")
print(f"Contagem de 80 a 90 anos: {contagem_80_90}")
print(f"Contagem de 90 a 100 anos: {contagem_90_100}")

# Encontrar o range com mais acidentes
faixas = {
    "10-20": contagem_10_20,
    "20-30": contagem_20_30,
    "30-40": contagem_30_40,
    "40-50": contagem_40_50,
    "50-60": contagem_50_60,
    "60-70": contagem_60_70,
    "70-80": contagem_70_80,
    "80-90": contagem_80_90,
    "90-100": contagem_90_100
}

# Encontrar a faixa etária com mais acidentes
faixa_com_mais_acidentes = max(faixas, key=faixas.get)
print('-------------------------------------')
print(f"Faixa etária com mais acidentes: {faixa_com_mais_acidentes} com {faixas[faixa_com_mais_acidentes]} acidentes")
print('-------------------------------------')
contagem_agrupada = df.groupby('Sex')['Age'].count()
print(f'Contagem por genero', contagem_agrupada)
print('-------------------------------------')

filtro = (df['Sex'] == 'Male') & (df['Age'] >= 30) & (df['Age'] <= 40) & (df['VehicleCategory'] == 'Sport')
quantidades = df[filtro].shape[0]
print(f"Quantidade de registros que se encaixam na categoria entre 30 e 40 anos com carros Sport: {quantidades}")
print('-------------------------------------')

filtro = (df['Sex'] == 'Male') & (df['Age'] >= 30) & (df['Age'] <= 40) & (df['VehicleCategory'] == 'Sedan')
quantidad = df[filtro].shape[0]
print(f"Quantidade de registros que se encaixam na categoria entre 30 e 40 anos com carros Sedan: {quantidad}")

print('-------------------------------------')

filtro = ((
	df['Sex'] == 'Male') &
	  (df['Age'] >= 30) & 
	  (df['Age'] <= 40) & 
	  (df['VehicleCategory'] == 'Sedan') &
	  (df['PastNumberOfClaims'] != '1')
	)
quantida = df[filtro].shape[0]
print(f"Quantidade de registros que se encaixam na categoria entre 30 e 40 anos com carros Sedan e já tiveram outras ocorrências anteriores: {quantida}")


filtro = (
	(df['Age'] >= 30) & 
	(df['Age'] <= 40) & 
	(df['VehicleCategory'] == 'Sedan') &
    (df['Sex'] == 'Female') &
	(df['Fault'] == 'Policy Holder')
	  )
quantid = df[filtro].shape[0]
print('-------------------------------------')

filtro = (
	(df['Age'] >= 30) & 
	(df['Age'] <= 40) & 
	(df['VehicleCategory'] == 'Sedan') &
	(df['Sex'] == 'Male') &
	(df['Fault'] == 'Policy Holder'))

quanti = df[filtro].shape[0]
print(f"Mulheres entre 30-40 anos com o carro Sedan e tem seguro : {quantid}")
print(f"Homens entre 30-40 anos com o carro Sedan e tem seguro: {quanti}")