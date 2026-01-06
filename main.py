import csv
import random
import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ===============================
# PARTE 1: CRIAR CSV SE NÃO EXISTIR
# ===============================
arquivo = "clientes.csv"

if not os.path.exists(arquivo):
    with open(arquivo, "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["ClienteID", "Idade", "Renda", "Divida", "Score", "Inadimplente"])
        for i in range(1, 21):
            idade = random.randint(18, 70)
            renda = random.randint(1000, 10000)
            divida = random.randint(0, 15000)
            score = random.randint(0, 100)
            inadimplente = random.randint(0, 1)
            escritor.writerow([i, idade, renda, divida, score, inadimplente])

# ===============================
# PARTE 2: LER O CSV
# ===============================
clientes = []
with open(arquivo) as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        clientes.append({
            "ClienteID": int(linha["ClienteID"]),
            "Idade": int(linha["Idade"]),
            "Renda": int(linha["Renda"]),
            "Divida": int(linha["Divida"]),
            "Score": int(linha["Score"]),
            "Inadimplente": int(linha["Inadimplente"])
        })

# ===============================
# PARTE 3: STREAMLIT INTERATIVO
# ===============================
st.title("Analisador de Créditos do Banco")

# Métricas gerais
media_idade = sum(c["Idade"] for c in clientes) / len(clientes)
media_renda = sum(c["Renda"] for c in clientes) / len(clientes)
media_divida = sum(c["Divida"] for c in clientes) / len(clientes)
perc_inadimplentes = sum(c["Inadimplente"] for c in clientes) / len(clientes) * 100

st.subheader("Métricas Gerais")
st.write(f"Média de idade: {int(media_idade)} anos")  # idade formatada
st.write(f"Média de renda: R$ {media_renda:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))  # formata como R$ 5.200,00
st.write(f"Média de dívida: R$ {media_divida:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))  # mesmo formato
st.write(f"% de inadimplentes: {perc_inadimplentes:.1f}%")

# Slider para filtrar clientes por score
score_min = st.slider("Score mínimo para filtrar clientes", 0, 100, 0)
clientes_filtrados = [c for c in clientes if c["Score"] >= score_min]
st.write(f"Clientes com score >= {score_min}: {len(clientes_filtrados)}")

# ===============================
# PARTE 4: GRÁFICO DE BARRAS POR FAIXA DE SCORE
# ===============================
# Criar faixas de score
faixas = list(range(0, 101, 10))  # 0, 10, 20, ..., 100
faixa_labels = [f"{faixas[i]}-{faixas[i+1]-1}" for i in range(len(faixas)-1)]
medias_divida = []
porc_inadimplentes = []

for i in range(len(faixas)-1):
    faixa_clientes = [c for c in clientes_filtrados if faixas[i] <= c["Score"] < faixas[i+1]]
    if faixa_clientes:
        media = sum(c["Divida"] for c in faixa_clientes) / len(faixa_clientes)
        inad = sum(c["Inadimplente"] for c in faixa_clientes) / len(faixa_clientes) * 100
    else:
        media = 0
        inad = 0
    medias_divida.append(media)
    porc_inadimplentes.append(inad)

# Plotar gráfico de barras
x = np.arange(len(faixa_labels))
fig, ax = plt.subplots(figsize=(10,5))
bars = ax.bar(x, medias_divida, color="skyblue", label="Média da Dívida")

# Destacar faixas com mais inadimplentes
for i, p in enumerate(porc_inadimplentes):
    if p > 0:
        bars[i].set_color("salmon")  # barra vermelha se houver inadimplentes

ax.set_xticks(x)
ax.set_xticklabels(faixa_labels, rotation=45)
ax.set_ylabel("Média da Dívida")
ax.set_xlabel("Faixa de Score")
ax.set_title("Média da Dívida por Faixa de Score (vermelho = clientes inadimplentes)")
ax.legend()
ax.grid(axis="y")

st.pyplot(fig)

st.markdown("---")  # linha horizontal
st.markdown("Projeto feito por **Bruna Machado** 💻")