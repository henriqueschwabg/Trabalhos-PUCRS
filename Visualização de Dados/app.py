import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

# 4

racacor_dataset = 'datasets/df_homicidios_racacor.csv'
sexo_dataset = 'datasets/df_homicidios_sexo.csv'
idade_dataset = 'datasets/df_homicidios_idade.csv'
escolaridade_dataset = 'datasets/df_homicidios_escolaridade.csv'


@st.cache
def load_data(dataset):

    data = pd.read_csv(dataset)
    return data


df_racacor = load_data(racacor_dataset)
df_sexo = load_data(sexo_dataset)
df_escolaridade = load_data(escolaridade_dataset)
df_idade = load_data(idade_dataset)

st.sidebar.markdown("**Números de homicídios por ano e estado**")

st.sidebar.subheader("Ano")
ano_filtrado = st.sidebar.slider("Escolha o ano desejado", 2008, 2018, 2017)

st.sidebar.subheader("Estado")
estados = sorted(df_racacor['UF'].unique())
estado_filtrado = st.sidebar.selectbox("Selecione o estado", estados)

st.sidebar.subheader("Filtro")
filtros = ["Escolaridade", "Faixa de Idade", "Raça/Cor", "Sexo"]
filtro_selecionado = st.sidebar.selectbox("Escolha o filtro", filtros)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Sistema de Informação sobre Mortalidade – SIM")
st.markdown(f"""
            ℹ️ Estão sendo exibidos os números de homicídios no estado do **{estado_filtrado}**
            para o ano de **{ano_filtrado}** e filtrados por **{filtro_selecionado}**.
            """)


if filtro_selecionado == 'Raça/Cor':
    df = df_racacor

    colunas_filtradas = [col for col in df if (col.startswith(str(ano_filtrado))) or (col in ['UF', 'lat', 'lon'])]
    dados_filtrados = df.loc[(df['UF'] == estado_filtrado), colunas_filtradas]

    colunas_filtradas = [col for col in df if col.startswith(str(ano_filtrado))]
    df_new = pd.DataFrame(dados_filtrados[colunas_filtradas].values.T)
    ax = df_new.plot.bar(color=[['blue', 'black', 'green', 'brown', 'maroon']])
    ax.set_title(f'Homicídios por {filtro_selecionado} em {ano_filtrado} no {estado_filtrado}')
    ax.set_xticklabels(('Branco', 'Preta', 'Amarela', 'Parda', 'Indígena'))
    ax.set_ylabel('quantidade')
    ax.get_legend().remove()

    st.pyplot()

elif filtro_selecionado == 'Sexo':
    df = df_sexo

    colunas_filtradas = [col for col in df if (col.startswith(str(ano_filtrado))) or (col in ['UF', 'lat', 'lon'])]
    dados_filtrados = df.loc[(df['UF'] == estado_filtrado), colunas_filtradas]
    colunas_filtradas = [col for col in df if col.startswith(str(ano_filtrado))]

    labels ='Homem', 'Mulher'
    explode = (0.1, 0)
    df_new = pd.DataFrame(dados_filtrados[colunas_filtradas].values.T)
    ax = df_new.plot.pie(subplots=True, explode=explode, labels=labels, autopct="%1.1f%%")
    plt.title(f'Homicídios por {filtro_selecionado} em {ano_filtrado} no {estado_filtrado}')
    plt.ylabel('')
    st.pyplot()

elif filtro_selecionado == 'Escolaridade':
    df = df_escolaridade

    colunas_filtradas = [col for col in df if (col.startswith(str(ano_filtrado))) or (col in ['UF', 'lat', 'lon'])]
    dados_filtrados = df.loc[(df['UF'] == estado_filtrado), colunas_filtradas]
    colunas_filtradas = [col for col in df if col.startswith(str(ano_filtrado))]

    df_new = pd.DataFrame(dados_filtrados[colunas_filtradas].values.T)
    ax = df_new.plot.bar(color=[['blue', 'black', 'green', 'brown', 'maroon']])
    ax.set_title(f'Homicídios por {filtro_selecionado} em {ano_filtrado} no {estado_filtrado}')
    ax.set_xticklabels(('Nenhuma', 'De 1 a 3 anos', 'De 4 a 7 anos', 'De 8 a 11 anos', '12 anos e mais'))
    ax.set_ylabel('quantidade')
    ax.get_legend().remove()

    st.pyplot()

elif filtro_selecionado == 'Faixa de Idade':
    df = df_idade

    colunas_filtradas = [col for col in df if (col.startswith(str(ano_filtrado))) or (col in ['UF', 'lat', 'lon'])]
    dados_filtrados = df.loc[(df['UF'] == estado_filtrado), colunas_filtradas]
    colunas_filtradas = [col for col in df if col.startswith(str(ano_filtrado))]

    df_new = pd.DataFrame(dados_filtrados[colunas_filtradas].values.T)
    ax = df_new.plot.bar(color=[['blue', 'black', 'green', 'brown', 'maroon']])
    ax.set_title(f'Homicídios por {filtro_selecionado} em {ano_filtrado} no {estado_filtrado}')
    ax.set_xticklabels(('0 - 4', '5 - 9', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39',
                        '40 - 44', '45 - 49', '50 - 54', '55 - 59', '60 - 64', '65 - 69', '70 - 74', '75 - 79', '80+'))
    ax.set_ylabel('quantidade')
    ax.get_legend().remove()

    st.pyplot()


### MAPA? ###
# st.subheader("Mapa do Estado")
# st.map(dados_filtrados)

# tabela (provavelmente temporária)
# st.sidebar.subheader("Tabela")
# tabela = st.sidebar.empty()
# if tabela.checkbox("Mostrar tabela de dados"):
    # st.write(dados_filtrados)

# 5 - Principais causas de mortes violentas por estado

causasviolentas_dataset = 'datasets/df_causas_violentas.csv'
df_causasviolentas = load_data(causasviolentas_dataset)

st.sidebar.markdown("**Principais causas de mortes violentas por estado**")

st.sidebar.subheader("Estado")
estados_causas = sorted(df_causasviolentas['UF'].unique())
estado_filtrado_causas = st.sidebar.selectbox("Selecione o estado*", estados_causas)

st.markdown(f"""
            ℹ️ Estão sendo exibidas as principais causas de mortes violentas no estado do **{estado_filtrado_causas}** entre 2008 e 2018.
            """)

grouped = df_causasviolentas[df_causasviolentas['UF'] == estado_filtrado_causas].groupby(['UF', 'descricao']).quantidade.sum().reset_index()
df_causasviolentas_new = pd.DataFrame(grouped)
df_causasviolentas_new.sort_values(by='quantidade', ascending=False, inplace=True)
df_causasviolentas_new.set_index('descricao', inplace=True)
plt.title(f'Principais causas de mortes violentas no estado do {estado_filtrado_causas}')
sns.barplot(x=df_causasviolentas_new['quantidade'][:5], y=df_causasviolentas_new[:5].index)
st.pyplot()

st.sidebar.markdown("""
                    A base de dados utilizada é gerenciada pelo ***Sistema de Informação sobre Mortalidade (SIM)***.
                    """)