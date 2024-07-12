      

def tratamento_CEO(dados):
    dados=__tratar_renomear_colunas(dados)
    dados=__tratar_inserir_nome_pais(dados)
    dados=__tratar_faixa_preco(dados)
    dados=__tratar_inserir_cor(dados)
    dados=__tratar_categorizar_restaurantes(dados)
    return dados


def __tratar_renomear_colunas(dados):
    #renomear colunas, remover espaços
    colunas=[i.replace(' ','_') for i in dados.columns]
    dados.columns=colunas
    return dados

def __tratar_inserir_nome_pais(dados):
    # colocar nomes dos países
    paises={
        1:'India',
        14:'Australia',
        30:'Brazil',
        37:'Canada',
        94:'Indonesia',
        148:'New Zeland',
        162:'Philippines',
        166:'Qatar',
        184:'Singapure',
        189:'South Africa',
        191:'Sri Lanka',
        208:'Turkey',
        214:'United Arab Emirates',
        215:'England',
        216:'United States of America'
    }
    dados['Country_name']=dados['Country_Code'].map(paises)
    return dados

def __tratar_faixa_preco(dados):
    def create_price_type(price_range):
        if price_range==1:
            return 'cheap'
        elif price_range==2:
            return 'normal'
        elif price_range==3:    
            return 'expensive'
        else:
            return 'gourmet'
    dados['Price_range']=dados['Price_range'].map(create_price_type)
    return dados

def __tratar_inserir_cor(dados):
    cores={
        "3F7E00":'darkgreen',
        '5BA829':'green',
        '9ACD32':'lightgreen',
        'CDD614':'orange',
        'FFBA00':'red',
        'CBCBC8':'darkred',
        'FF7800':'darkred'
    }
    dados['Rating_color']=dados['Rating_color'].map(cores)
    return dados

def __tratar_categorizar_restaurantes(dados):
    dados['main_Cuisines']=dados['Cuisines'].map(lambda x:str(x).split(',')[0])
    return dados
