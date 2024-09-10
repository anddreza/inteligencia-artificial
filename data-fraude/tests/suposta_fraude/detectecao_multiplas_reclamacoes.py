import pandas as pd

dados = pd.read_csv('fraud.csv')
df = pd.DataFrame(dados)


# Verificar se há usuários que fazem múltiplas reclamações em um curto espaço de tempo
reclamacoes_por_usuario = df.groupby('UsuarioID')['ReclamacaoID'].count()
high_claims = reclamacoes_por_usuario[reclamacoes_por_usuario > 3]  # Exemplo: mais de 3 reclamações
print(high_claims)
