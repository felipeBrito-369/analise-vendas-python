import pandas as pd
import matplotlib.pyplot as plt
import random

# 1. Gerar dados fictícios de vendas
random.seed(42)

produtos = {
    "Notebook": 3500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 900,
    "Headset": 250,
}

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun",
         "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

linhas = []
for mes in meses:
    for produto, preco in produtos.items():
        quantidade = random.randint(5, 40)
        linhas.append({
            "mes": mes,
            "produto": produto,
            "quantidade": quantidade,
            "receita": quantidade * preco,
        })

df = pd.DataFrame(linhas)
df.to_csv("vendas.csv", index=False)

# 2. Conhecer os dados
print("Primeiras linhas:")
print(df.head())
print()

# 3. Análises
receita_produto = df.groupby("produto")["receita"].sum().sort_values(ascending=False)
receita_mes = df.groupby("mes")["receita"].sum().reindex(meses)

print("Receita por produto:")
print(receita_produto)
print()
print("Receita por mês:")
print(receita_mes)
print()
print(f"Receita total: R$ {df['receita'].sum():,.2f}")
print(f"Produto mais vendido (unidades): {df.groupby('produto')['quantidade'].sum().idxmax()}")
print(f"Melhor mês: {receita_mes.idxmax()}")

# 4. Gráfico 1: receita por produto
receita_produto.plot(kind="bar", color="#9370DB")
plt.title("Receita total por produto")
plt.xlabel("Produto")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico_produtos.png")
plt.close()

# 5. Gráfico 2: receita por mês
receita_mes.plot(kind="line", marker="o", color="#9370DB")
plt.title("Receita mensal")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.tight_layout()
plt.savefig("grafico_meses.png")
plt.close()

print("\nGráficos salvos com sucesso!")