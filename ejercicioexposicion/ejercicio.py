import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = [
    ["Juan", "Baja", "Media"],
    ["Pedro", "Alta", "Media"],
    ["Luis", "Media", "Alta"],
    ["Juan", "Media", "Baja"],
    ["Pedro", "Baja", "Baja"],
    ["Luis", "Media", "Alta"],
    ["Juan", "Baja", "Media"],
    ["Pedro", "Alta", "Media"],
    ["Luis", "Media", "Baja"],
]

te = TransactionEncoder()
te_ary = te.fit(data).transform(data)

df = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.3)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

print("Conjuntos Frecuentes:")
print(frequent_itemsets)

print("\nReglas de Asociacion:")
print(rules)
