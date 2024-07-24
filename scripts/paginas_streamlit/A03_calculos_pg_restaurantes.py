#========================================================
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



#========================================================
