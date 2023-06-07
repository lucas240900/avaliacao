import streamlit as st
import pandas as pd

st.write("Analise de Jogos");
df = pd.read_csv("C:/Users/Usuario/Desktop/avaliacao.csv");
st.subheader("Informações dos dados");

x = df.drop(['Outcome'],1);
y = df['Outcome'];

def get_user_date():
    Rank = st.sidebar.slider ("Ranking geral de vendas"),
    Name = st.sidebar.slider ("Nome do jogo"),
    Platform = st.sidebar.slider ("Plataforma"),
    Year = st.sidebar.slider ("Ano de lançamento"),
    Genre = st.sidebar.slider ("Genero do jogo"),
    Publisher= st.sidebar.slider ("Editora do joogo"),
    NA_Sales = st.sidebar.slider ("Vendas na America do Norte"),
    EU_Sales = st.sidebar.slider ("Vendas na União Europeia"),
    JP_Sales = st.sidebar.slider ("Vendas no Japão"),
    Other_Sales = st.sidebar.slider ("Vendas em outros lugares do mundo"),
    Global_Sales = st.sidebar.slider ("Total de vendas no mundo inteiro");

user_data = {'Rankins geral de vendas': rank,
    'Nome': name,
    'Plataforma': platform,
    'Ano de lançamento': year,
    'Genero do jogo': genre,
    'Editora do jogo': publisher,
    'Vendas na America do Norte': na_sales,
    'Vendas na União Europeia': eu_sales,
    'Vendas no Japão': jp_sales,
    'Vendas em outros lugares do mundo': other_sales,
    'Total de vendas no mundo inteiro': global_sales
    }

features = pd.DataFrame(user_data, index=[0]);
return features;

user_input_variables = get_user_date();

graf = st.bar_chart(user_input_variables);
dtc = DecisionTreeClassifier(criterion='entropy', max_depth=3);
dtc.fit(x_train, y_train);
    