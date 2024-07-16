def tratamento_cientista(dados):
    #tratamento aplicado pelo cientista de dados
    dados=__moeda_dolar(dados)
    dados=__valores_boleanos(dados)
    dados=__limpar_dados(dados)

    #remover colunas sem valor
    dados=dados.drop(columns=['Switch_to_order_menu'])

    return dados



def __moeda_dolar(dados):
    """Essas taxas de câmbio foram obtidas de fontes confiáveis e refletem os
      valores aproximados atuais(XE) (X-Rates ). Pesquisa feita pelo ChatGPT  """
    #correção do custo no preço Average_Cost_for_two para dolar
    exchange_rates = {
        'Botswana Pula(P)': 0.075,  # 1 Pula = 0.075 USD
        'Brazilian Real(R$)': 0.205,  # 1 Real = 0.205 USD
        'Dollar($)': 1.0,  # 1 USD = 1 USD
        'Emirati Diram(AED)': 0.272,  # 1 AED = 0.272 USD
        'Indian Rupees(Rs.)': 0.012,  # 1 INR = 0.012 USD
        'Indonesian Rupiah(IDR)': 0.000066,  # 1 IDR = 0.000066 USD
        'NewZealand($)': 0.608,  # 1 NZD = 0.608 USD
        'Pounds(£)': 1.291,  # 1 GBP = 1.291 USD
        'Qatari Rial(QR)': 0.275,  # 1 QAR = 0.275 USD
        'Rand(R)': 0.056,  # 1 ZAR = 0.056 USD
        'Sri Lankan Rupee(LKR)': 0.0033,  # 1 LKR = 0.0033 USD
        'Turkish Lira(TL)': 0.030,  # 1 TRY = 0.030 USD
    }
    dados['Average_Cost_for_two']=dados['Currency'].map(exchange_rates)*dados['Average_Cost_for_two']
    return dados

def __valores_boleanos(dados):
    #alterar boleanos para sim/não
    sim_nao={
        1:'YES',
        0:'NO'
    }
    colunas=['Has_Table_booking','Has_Online_delivery', 'Is_delivering_now']

    for col in colunas:
        dados[col]=dados[col].map(sim_nao)

    return dados

def __limpar_dados(dados):
    #remover outlier
    dados=dados.copy()

    filtro=((dados['Average_Cost_for_two']==25000017)&
            (dados['Restaurant_ID']==16608070))
    dados=dados[~filtro]


    return dados