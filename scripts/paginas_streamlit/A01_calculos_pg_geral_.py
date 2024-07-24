def unique_restaurants(dados):
    answer=len(dados['Restaurant_ID'].drop_duplicates())
    return answer
def unique_contries(dados):
    answer=len(dados['Country_name'].drop_duplicates())
    return answer
def unique_cities(dados):
    answer=len(dados['City'].drop_duplicates())
    return answer
def unique_votes(dados):
    answer=len(dados['Votes'].drop_duplicates())
    return answer
def unique_cuisines(dados):
    answer=len(dados['main_Cuisines'].drop_duplicates())
    return answer
def list_of_restaurants(dados):
    aux_df=dados.copy()
    aux_df['Restaurant_ID']=aux_df['Restaurant_ID'].astype(str)
    aux_df=aux_df.set_index('Restaurant_ID')
    columns= {  'Restaurant_Name':'Name',
                'Country_name':'Country',
                'City':'City',
                'Votes':'Votes',
                'main_Cuisines':'main_Cuisines'}
    aux_df=aux_df[columns.keys()].rename(columns=columns)
    aux_df=aux_df.drop_duplicates()

    return aux_df