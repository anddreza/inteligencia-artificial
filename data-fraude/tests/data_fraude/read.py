import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)

contagem_agrupada = df.groupby('Sex')['Age'].count()
contagem_veiculo = df['VehicleCategory'].value_counts()


print(f'Contagem por genero', contagem_veiculo)
print('-------------------------------------')

contagem_veiculos_envolvidos = df['NumberOfCars'].value_counts()
#contagem_veiculos_envolvidos_com_testemunha = df.groupby('NumberOfCars')['WitnessPresent'].value_counts()
print('Contagem de veiculos envolvidos', contagem_veiculos_envolvidos)
print('-------------------------------------')

filtro = df['WitnessPresent'] == 'Yes'
# quantidade_de_carros = df[filtro]['NumberOfCars'].sum()
# print(f"Quantidade total de carros envolvidos em acidentes com testemunhas presentes: {quantidade_de_carros}")


