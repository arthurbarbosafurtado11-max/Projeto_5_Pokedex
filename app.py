# IMPORTAMDO DE BIBLIOTECAS 
import pandas as pd
import streamlit as st
import json
import requests

## ajustando o layout da pagina
st.set_page_config(layout='wide')

# lendo o arquivo jsonpokemon_index
with open('pokemon_index.json', 'r', encoding='utf-8') as arquivo:
    nomes_pokemons = json.load(arquivo)

# Criando uma caixa seletora onde a pessoa possa escolher o pokemon pelo nome
nome = st.selectbox('Escolha o seu Pokemon :', nomes_pokemons.values())

# link da api
url = f'https://pokeapi.co/api/v2/pokemon/{nome}'

# usando todas as informarçoes da API
dados_pokemon = requests.get(url).json()

# vamos criar colunas no site
col1, col2, col3 = st.columns(3)

peso = dados_pokemon['weight'] /10
altura = dados_pokemon['height'] /10
imc = round(peso / (altura ** 2))

# Pegando a imagem do pokemon
with col1:
    st.image(dados_pokemon['sprites']['front_default'],width=550)

with col2:
    st.audio(dados_pokemon['cries']['latest'])
    st.audio(dados_pokemon['cries']['legacy'])

with col3:
    st.image(dados_pokemon['sprites']['front_shiny'], width= 550)
    st.write('shiny')

# Recriando as colunas para informações de peso, altura e IMC
col1,col2,col3 = st.columns(3)

with col1:
    st.metric(f"O Peso do Pokemon é :",peso)

with col2:
    st.metric(f"A Altura do Pokemon é :",altura)

with col3:
    st.metric(f"O IMC é :",imc)

status,tipos,habilidades,locais = st.tabs(['Status','Tipos','Habilidades','locais'])

with tipos:
    for i in dados_pokemon['types']:
        st.markdown(f'- {i['type']['name']}')

with status:
    hp, ataque, defesa, ataque_esp, defesa_esp, velocidade = st.columns(6)
    with hp:
        st.metric('HP', dados_pokemon['stats'][0]['base_stat'])
    with ataque:
        st.metric('Ataque', dados_pokemon['stats'][1]['base_stat'])
    with defesa:
        st.metric('Defesa', dados_pokemon['stats'][2]['base_stat'])
    with ataque_esp:
        st.metric('Ataque Especial', dados_pokemon['stats'][3]['base_stat'])
    with defesa_esp:
        st.metric('Defesa Especial', dados_pokemon['stats'][4]['base_stat'])
    with velocidade:
        st.metric('Velocidade', dados_pokemon['stats'][5]['base_stat'])

with locais:
    locais = requests.get(dados_pokemon['location_area_encounters']).json()
    for local in locais:
        st.markdown(f'-{local['location_area']['name']}')

with habilidades:
    for habilidade in dados_pokemon['abilities']:
        st.markdown(f'- {habilidade['ability']['name']}')





