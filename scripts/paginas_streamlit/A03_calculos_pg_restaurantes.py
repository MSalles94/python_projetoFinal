#========================================================
#general number - first line
def registred_restaurants(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID']].drop_duplicates()
    aux_df=len(aux_df['Restaurant_ID'])
    return aux_df


def avg_price_forTwo(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID','Average_Cost_for_two']].drop_duplicates()

    return aux_df['Average_Cost_for_two'].mean().round(2)

def num_votes(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID','Votes']].drop_duplicates()

    return aux_df ['Votes'].sum()

def total_rate(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID','Votes','Aggregate_rating']].drop_duplicates()
    aux_df['total_range']=aux_df['Votes']*aux_df['Aggregate_rating']


    return  (aux_df['total_range'].sum()/aux_df['Votes'].sum()).round(3)

#========================================================
#general number - second line

def accept_booking(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID','Has_Table_booking']].drop_duplicates()
    aux_df=aux_df[aux_df['Has_Table_booking']=='YES']

    return  aux_df['Restaurant_ID'].count()

def accept_online_delivery(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID','Has_Online_delivery']].drop_duplicates()
    aux_df=aux_df[aux_df['Has_Online_delivery']=='YES']

    return  aux_df['Restaurant_ID'].count()

def accept_delivery(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Restaurant_ID','Is_delivering_now']].drop_duplicates()
    aux_df=aux_df[aux_df['Is_delivering_now']=='YES']

    return  aux_df['Restaurant_ID'].count()

#========================================================
#lists rating

def botton_brasilien_restaurants(dados):

    aux_df=dados.copy()
    aux_df=aux_df[aux_df['main_Cuisines']=='Brazilian']
    aux_df=aux_df[['Restaurant_Name','Aggregate_rating']].drop_duplicates()
    aux_df=aux_df.sort_values(by='Aggregate_rating')
    aux_df=aux_df.reset_index(drop=True)
    aux_df.index=aux_df.index+1
    aux_df.columns=['Restaurant','Rate']
    return aux_df[:20]

def top_brasilien_restaurants(dados):

    aux_df=dados.copy()
    aux_df=aux_df[aux_df['main_Cuisines']=='Brazilian']
    aux_df=aux_df[aux_df['Country_name']=='Brazil']
    aux_df=aux_df[['Restaurant_Name','Aggregate_rating']].drop_duplicates()
    aux_df=aux_df.sort_values(by='Aggregate_rating',ascending=False)
    aux_df=aux_df.reset_index(drop=True)
    aux_df.index=aux_df.index+1
    aux_df.columns=['Restaurant','Rate']
    return aux_df[:20]

#========================================================

#some graphs
def top_avg_price(dados):

    from plotly.express import bar

    dados=dados[['Restaurant_ID','Restaurant_Name','Average_Cost_for_two']].drop_duplicates()
    dados=dados.groupby(['Restaurant_Name'])[['Average_Cost_for_two']].sum().sort_values(by='Average_Cost_for_two',ascending=False)
    dados=dados[:10].reset_index()

    fig=bar(dados,y='Restaurant_Name',x='Average_Cost_for_two', orientation='h',color='Restaurant_Name')
    fig.update_layout(showlegend=False)
    return fig

#========================================================
def avg_votes_online(dados):

    from plotly.express import bar

    dados=dados[['Restaurant_ID','Has_Online_delivery','Votes']].drop_duplicates().copy()
    dados['Restaurant_ID']=1
    dados=dados.groupby(['Has_Online_delivery']).sum().reset_index()
    dados['AVG_votes']=dados['Votes']/dados['Restaurant_ID']
    fig=bar(dados,x='Has_Online_delivery',y='AVG_votes',color='Has_Online_delivery')
    fig.update_layout(showlegend=False)

    return fig


def avg_cost_booking(dados):

    from plotly.express import bar

    dados=dados[['Restaurant_ID','Has_Table_booking','Average_Cost_for_two']].drop_duplicates().copy()
    dados=dados.groupby(['Has_Table_booking']).mean().reset_index()

    fig=bar(dados,x='Has_Table_booking',y='Average_Cost_for_two',color='Has_Table_booking')
    fig.update_layout(showlegend=False)

    return fig

def cost_BBQ_verus_japa(dados):
    from plotly.express import bar

    dados=dados[dados['Country_name'].isin(['United States of America'])].copy()

    dados=dados[['Restaurant_ID','main_Cuisines','Average_Cost_for_two']].drop_duplicates().copy()


    japa_usa=dados['main_Cuisines'].isin(['Japanese'])
    bbq_usa=dados['main_Cuisines'].isin(['BBQ'])

    dados.loc[japa_usa,'Type']='USA Japanese'
    dados.loc[bbq_usa,'Type']='USA BBQ'
    dados=dados[~dados['Type'].isna()]
    dados=dados.groupby(['Type'])[['Average_Cost_for_two']].sum().reset_index()


    fig=bar(dados,x='Type',y='Average_Cost_for_two',color='Type')
    fig.update_layout(showlegend=False)


    return fig


#========================================================

#   CUISINE

def cuisine_value_for_two(dados):
    aux_df=dados[['main_Cuisines','Restaurant_ID','Average_Cost_for_two']].drop_duplicates()
    aux_df=aux_df.groupby(['main_Cuisines'])[['Average_Cost_for_two']].mean().sort_values(by='Average_Cost_for_two',ascending=False)
    aux_df=aux_df.reset_index()[:20]

    from plotly.express import bar

    y='main_Cuisines'
    x='Average_Cost_for_two'

    fig=bar(aux_df,x,y,color='main_Cuisines')
    fig.update_layout(showlegend=False)


    return fig

def cuisine_avg_rate(dados):
    aux_df=dados[['main_Cuisines','Restaurant_ID','Aggregate_rating']].drop_duplicates()
    aux_df=aux_df.groupby(['main_Cuisines'])[['Aggregate_rating']].mean().sort_values(by='Aggregate_rating',ascending=False)
    aux_df=aux_df.reset_index()[:20]

    from plotly.express import bar

    y='main_Cuisines'
    x='Aggregate_rating'

    fig=bar(aux_df,x,y,color='main_Cuisines')
    fig.update_layout(showlegend=False)


    return fig

def cuisine_online_delivers(dados):
    aux_df=dados[['main_Cuisines','Restaurant_ID','Has_Online_delivery','Is_delivering_now']].drop_duplicates()
    aux_df=aux_df[aux_df['Has_Online_delivery']=='YES']
    aux_df=aux_df[aux_df['Is_delivering_now']=='YES']
    column_name='Online Delivers'
    aux_df[column_name]=1

    aux_df=aux_df.groupby(['main_Cuisines'])[[column_name]].sum().sort_values(by=column_name,ascending=False)[:20].reset_index()



    from plotly.express import bar

    y='main_Cuisines'
    x=column_name
    fig=bar(aux_df,x,y,color='main_Cuisines')
    fig.update_layout(showlegend=False)

    return fig

#========================================================
def top_rating_cuisine(dados,filter_c,worst_rating=True):

    aux_df=dados.loc[dados['main_Cuisines'].isin(filter_c),['Restaurant_ID','Restaurant_Name','Aggregate_rating']].copy().drop_duplicates()
    aux_df=aux_df.sort_values(by='Aggregate_rating',ascending=worst_rating).reset_index(drop=True)
    aux_df.index+=1

    if worst_rating:
        valor_ref=(aux_df['Aggregate_rating']==aux_df['Aggregate_rating'].min()).sum()
    else:
        valor_ref=(aux_df['Aggregate_rating']==aux_df['Aggregate_rating'].max()).sum()

    print(aux_df['Aggregate_rating'].max())
 
    if valor_ref>20:
        aux_df=aux_df[:valor_ref]
    else:
        aux_df=aux_df[:20]
    


    return aux_df

#========================================================

