class ler_dados():
    def __init__(self):
        self.leitura()

    def leitura(self):
        from pandas import read_csv
        dados=read_csv('./dataset/zomato.csv')
        self.dados=dados
        
        def pre_tratamento(): 
            #tratamento sugerido pelo CEO
            self.__tratar_renomear_colunas()
            self.__tratar_inserir_nome_pais()
            self.__tratar_faixa_preco()
            self.__tratar_inserir_cor()
            self.__tratar_categorizar_restaurantes()
        pre_tratamento()
        
    def __tratar_renomear_colunas(self):
        dados=self.dados
        #renomear colunas, remover espaços
        colunas=[i.replace(' ','_') for i in dados.columns]
        dados.columns=colunas

    def __tratar_inserir_nome_pais(self):
        dados=self.dados
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

    def __tratar_faixa_preco(self):
        dados=self.dados

        def create_price_type(price_range):
            if price_range==1:
                return 'cheap'
            elif price_range==2:
                return 'normal'
            elif price_range==3:    
                return 'expencive'
            else:
                return 'gourmet'
            
        dados['Price_range']=dados['Price_range'].map(create_price_type)

    def __tratar_inserir_cor(self):
        dados=self.dados
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

    def __tratar_categorizar_restaurantes(self):
        dados=self.dados
        dados['Cuisines']=dados['Cuisines'].map(lambda x:str(x).split(',')[0])

    def exportar_df(self):
        return self.dados
