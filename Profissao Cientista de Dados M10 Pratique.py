import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())

#Grafico de dispersão
plt.hexbin(df['Nota'], df['N_Avaliações'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Nota')
plt.ylabel('N_Avaliações')
plt.title('Dispersão de Nota e Número de Avaliações')
plt.show()

#Mapa de Calor
corr = df[['Preço', 'Nota', 'N_Avaliações', 'Qtd_Vendidos_Cod']].corr()
plt.subplot(2,2,3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação preço, nota, Nº de avaliações e Qtde de vendidos')

#Gráfico de barras
plt.figure(figsize=(10,6))
df['Gênero'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Relação de Gênero e quantidades')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

#Gráfico de pizza
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values
plt.figure(figsize=(10,6))
plt.pie(y, labels=x, autopct = '%.1f%%', startangle=90)
plt.title('Distribuição de Gênero')
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'],fill=True, color='#863e9c')
plt.title('Densidade de Notas')
plt.xlabel('Notas')
plt.show()