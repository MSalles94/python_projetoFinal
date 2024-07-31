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


#========================================================
