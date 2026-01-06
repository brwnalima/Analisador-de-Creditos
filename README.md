# Analisador de Créditos do Banco 💳

Este é um projeto de **análise de risco de crédito** feito em Python com **Streamlit**, onde é possível:

- Gerar uma base fictícia de clientes de um banco
- Calcular métricas gerais como média de idade, renda, dívida e % de inadimplentes
- Visualizar clientes de maior risco com gráficos interativos
- Filtrar clientes por faixa de score e ver tendências de inadimplência

O app é totalmente interativo e pode ser usado tanto localmente quanto via web.

---

## 📊 Funcionalidades

- Criação automática de CSV com dados fictícios de clientes
- Cálculo de métricas gerais:
  - Média de idade
  - Média de renda
  - Média de dívida
  - % de inadimplentes
- Gráfico de barras mostrando **média da dívida por faixa de score**, destacando faixas com clientes inadimplentes
- Slider interativo para filtrar clientes por score
- Rodapé com informação do autor

---

## 🚀 Tecnologias utilizadas

- Python 3  
- Streamlit  
- Matplotlib  
- Numpy  
- CSV (para armazenamento de dados)

---

## 💻 Como rodar localmente

1. Clone o repositório:

```bash
git clone https://github.com/brwnalima/Analisador-de-Creditos.git
cd Analisador-de-Creditos
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
```

3. Ative o ambiente:

Windows:

```bash
venv\Scripts\activate
```
Linux/Mac:

```bash
source venv/bin/activate
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Rode o app:

```bash
streamlit run main.py
```

6. Quando terminar, saia do ambiente virtual:

```bash
deactivate
```

7. Para fechar o terminal completamente:

```bash
exit
```

---

## 🌐 Deploy online

O app está disponível no Streamlit Community Cloud: https://6doaj3mnucss2xfujwnfx3.streamlit.app/

---

## 👩‍💻 Autor
Projeto feito por Bruna Machado 💻
