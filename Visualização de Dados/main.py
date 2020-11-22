import streamlit as st
import pandas as pd

racacor_dataset = 'datasets/df_homicidios_racacor.csv'
sexo_dataset = 'datasets/df_homicidios_sexo.csv'


@st.cache
def load_data(dataset):

    data = pd.read_csv(dataset)
    return data


df_racacor = load_data(racacor_dataset)
df_sexo = load_data(sexo_dataset)


st.sidebar.header("Parâmetros")
info_sidebar = st.sidebar.empty()

st.sidebar.subheader("Ano")
ano_filtrado = st.sidebar.slider("Escolha o ano desejado", 2008, 2018, 2017)

## se forem todos os anos????

st.sidebar.subheader("Estado")
estados = sorted(df_racacor['UF'].unique())
estado_filtrado = st.sidebar.selectbox("Selecione o estado", estados)

st.sidebar.subheader("Filtro")
filtros = ["Raça/Cor", "Sexo"]
filtro_selecionado = st.sidebar.selectbox("Escolha o filtro", filtros)

st.sidebar.markdown("""
                    A base de dados utilizada é gerenciada pelo ***Sistema de Informação sobre Mortalidade (SIM)***.
                    """)

if filtro_selecionado == 'Raça/Cor':
    df = df_racacor
elif filtro_selecionado == 'Sexo':
    df = df_sexo

colunas_filtradas = [col for col in df if (col.startswith(str(ano_filtrado))) or (col in ['UF', 'lat', 'lon'])]
dados_filtrados = df.loc[(df['UF'] == estado_filtrado), colunas_filtradas]

# info_sidebar.info(np.sum(dados_filtrados[])

st.title("Sistema de Informação sobre Mortalidade – SIM")
st.markdown(f"""
            ℹ️ Estão sendo exibidos os números de homicídios no estado do **{estado_filtrado}**
            para o ano de **{ano_filtrado}** e filtrados por **{filtro_selecionado}**.
            """)

# tabela (provavelmente temporária)
st.sidebar.subheader("Tabela")
tabela = st.sidebar.empty()

if tabela.checkbox("Mostrar tabela de dados"):
    st.write(dados_filtrados)

colunas_filtradas = [col for col in df if col.startswith(str(ano_filtrado))]
st.bar_chart(dados_filtrados[colunas_filtradas])

st.subheader("Mapa do Estado")
st.map(dados_filtrados)