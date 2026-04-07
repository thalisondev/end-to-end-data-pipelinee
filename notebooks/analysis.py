import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/curated/curated_sales.csv")

sales_by_product = df.groupby("product")["total_value"].sum().sort_values(ascending=False)

plt.figure()

bars = plt.bar(sales_by_product.index, sales_by_product.values)

# destaca o maior
max_index = sales_by_product.values.argmax()
bars[max_index].set_alpha(0.5)

# valores no gráfico
for i, v in enumerate(sales_by_product):
    plt.text(i, v, f"R${v:.2f}", ha='center', va='bottom')

plt.title("Análise de Receita por Produto", fontsize=14)
plt.xlabel("Produto")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45)

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()