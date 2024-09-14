import pandas as pd 

df = pd.read_json('./Teste 3/dados.json')
df.set_index('dia', inplace=True)

df_valor_maior_zero = df[df['valor'] > 0]

menor_valor = df_valor_maior_zero['valor'].min()
maior_valor = df_valor_maior_zero['valor'].max()
media_mensal = df_valor_maior_zero['valor'].mean()

dias_acima_da_media = len(df_valor_maior_zero['valor'] > media_mensal)

print(f'Menor faturamento: {menor_valor}')
print(f'Maior faturamento: {maior_valor}')
print(f'Dias com faturamento acima da média: {dias_acima_da_media}')


