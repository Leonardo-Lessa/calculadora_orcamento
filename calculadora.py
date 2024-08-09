import streamlit as st
import pandas as pd
import numpy as np


#lendo base de dados e montando lista de materias
database = pd.read_csv(r'data/base.csv')
options_list = database['material'].unique().tolist()


st.title('Calculadora de Orçamento') # titulo

options = st.multiselect(
    'Escolha os materiais:',
    options_list
)

if len(options) == 0: # gambiarra para nao exibir mensagem de erro enquanto nao tiver valor em optinos
    pass
else:
    quantidade_list = []
    margem_list = []
    custo_list = []
    lucro_list = []
    preco_list = []
    def input_quantidade(options): # inputando quantidades
        for option in options:
            quantidade_list.append(st.number_input('Quantidade (em metros quadrados) de ' + option, min_value=0))      
        return quantidade_list
    def input_custo(options): # inputando custos
        for option in options:
            custo_list.append(st.number_input('Custo (em R$)de ' + option, min_value=0))
        return custo_list
    def input_margem(options): # inputando margem de lucro desejada
        for option in options:
            margem_list.append(st.number_input('Margem de lucro (%) desejada para ' + option, min_value=0))
        return margem_list
    def print_preco(options): # calculando o preco a ser cobrado pra cada item
        for custo, quantidade, margem in zip(custo_list, quantidade_list, margem_list):
            preco = (custo * quantidade) * (margem/100 +1)
            preco = round(preco, 2)
            preco_list.append(preco)
        for option, preco in zip(options, preco_list):
            st.write(option + ': R$' + str(preco))
        return preco_list
    def lucro_final(quantidade_list, preco_list, custo_list): # calculando o lucro final
        for quantidade, preco, custo in zip(quantidade_list, preco_list, custo_list):
            lucro = preco - (custo * quantidade)
            lucro_list.append(lucro)
        return lucro_list
    input_quantidade(options)
    input_margem(options)
    input_custo(options)
    if st.button('Calcular orçamento:'):
        print_preco(options)
    if len(preco_list) == 0:
        pass
    else:
        st.write('Preço final a ser cobrado: R$' + str(round(sum(preco_list), 2))) # calculando o preco final total a ser cobrado
        lucro_final(quantidade_list, preco_list, custo_list)
        st.write('Lucro total no serviço: R$' + str(round(sum(lucro_list), 2)))  # calculando o lucro total 
    
