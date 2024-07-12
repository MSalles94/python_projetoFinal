def ler_dados():
    #leitura e tratamento dos dados
    from pandas import read_csv
    dados=read_csv('./dataset/zomato.csv')

    #tratamento de dados sugerido pelo CEO
    from scripts.manipular_dados.A01_alteracoes_CEO import tratamento_CEO
    dados=tratamento_CEO(dados)

    #tratamento de dados feito pelo cientista de dados
    from scripts.manipular_dados.A02_alteracoes_extras import tratamento_cientista
    dados=tratamento_cientista(dados)


    return dados


