#================================================

#=======================================
#MAIN NUMBERS
#=======================================
def registred_cities(dados):
    aux_df=dados[["Country_name",'City']].drop_duplicates()
    aux_df=aux_df['City'].count()

    return aux_df

def registred_restaurants(dados):
    aux_df=dados["Restaurant_ID"].unique()
    aux_df=len(aux_df)

    return aux_df

def total_votes(dados):
    aux_df=dados[['Restaurant_ID',"Votes"]].drop_duplicates()
    aux_df=aux_df['Votes'].sum()

    return aux_df

def total_cuisines(dados):
    aux_df=dados["main_Cuisines"].unique()
    aux_df=len(aux_df)

    return aux_df

def avg_price_for_two(dados):
    aux_df=dados[['Restaurant_ID',"Average_Cost_for_two"]].drop_duplicates()
    aux_df=round(aux_df['Average_Cost_for_two'].mean(),2)

    return aux_df
#=======================================
#=======================================
#COUNTRIES
#=======================================
#=======================================
#DATAFRAME WITH GENERAL INFORMATIONS
#=======================================


def generate_geral_df(dados):

    def col_cities(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','City']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).count()
        aux_df.columns=['Cities']
        return aux_df

    def col_restaurants(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','Restaurant_ID']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).count()
        aux_df.columns=['Restaurants']
        return aux_df

    def col_gourmetRestaurants(dados):
        aux_df=dados.copy()
        aux_df=aux_df[aux_df['Price_range']=='gourmet']
        aux_df=aux_df[['Country_name','Restaurant_ID']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).count()
        aux_df.columns=['Gourmet_restaurants']
        return aux_df

    def col_cuisines(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','main_Cuisines']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).count()
        aux_df.columns=['cuisines']
        return aux_df

    def col_totalVotes(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','Restaurant_ID',"Votes"]].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name'])[['Votes']].sum()
        aux_df.columns=['total_votes']
        return aux_df

    def col_isDelivering(dados):
        aux_df=dados.copy()
        aux_df=aux_df[aux_df['Is_delivering_now']=='YES']
        aux_df=aux_df[['Country_name','Restaurant_ID']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).count()
        aux_df.columns=['Delivering_restaurants']
        return aux_df

    def col_hasBooking(dados):
        aux_df=dados.copy()
        aux_df=aux_df[aux_df['Has_Table_booking']=='YES']
        aux_df=aux_df[['Country_name','Restaurant_ID']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).count()
        aux_df.columns=['booking_restaurants']
        aux_df=aux_df.astype(int)
        return aux_df

    def col_MeanVotes_perCountry(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','Restaurant_ID','Votes']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name'])[['Votes']].mean()
        aux_df=aux_df.round(0)
        aux_df.columns=['Mean_votes']
        return aux_df

    def col_meanRate(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','Restaurant_ID','Votes','Aggregate_rating']].drop_duplicates()
        aux_df['mean_rate']=aux_df['Votes']*aux_df['Aggregate_rating']
        aux_df=aux_df.groupby(['Country_name']).mean()
        aux_df['mean_rate']=aux_df['mean_rate']/aux_df['Votes']
        aux_df=aux_df[['mean_rate']]
        return aux_df

    def col_avgPrice_two(dados):
        aux_df=dados.copy()
        aux_df=aux_df[['Country_name','Restaurant_ID','Average_Cost_for_two']].drop_duplicates()
        aux_df=aux_df.groupby(['Country_name']).agg({'Restaurant_ID':'count','Average_Cost_for_two':'sum'})
        aux_df['avg_price_forTwo']=aux_df['Average_Cost_for_two']/aux_df['Restaurant_ID']
        aux_df=aux_df[['avg_price_forTwo']].round(2)
        return aux_df


    def dataframe_geral(dados):
        colunas={}
        colunas['cities']=col_cities(dados)
        colunas['cuisines']=col_cuisines(dados)
        #restaurants
        colunas['restaurants']=col_restaurants(dados)
        colunas['gourmet_restaurants']=col_gourmetRestaurants(dados)
        colunas['Delivering_restaurants']=col_isDelivering(dados)
        colunas['booking_restaurants']=col_hasBooking(dados)
        colunas['avg_price_forTwo']=col_avgPrice_two(dados)
        #votes and rating
        colunas['total_votes']=col_totalVotes(dados)
        colunas['Mean_votes']=col_MeanVotes_perCountry(dados)
        colunas['Mean_rate']=col_meanRate(dados)
        from pandas import concat
        colunas=concat(list(colunas.values()),axis=1)
        colunas=colunas.reset_index().fillna(0)
        return colunas

    return dataframe_geral(dados)

#=======================================
#graphs
#=======================================
def grafico_cities(dados):
    from plotly.express import bar
    aux_df=dados[['Country_name','City']].drop_duplicates()
    aux_df=aux_df.groupby(['Country_name']).count().reset_index().sort_values(by='City',ascending=False)

    fig=bar(aux_df,x='Country_name',y='City')
    return fig

def graph_deliver_or_booking(dados):
    from plotly.express import pie
    aux_df=dados[['Restaurant_ID','Is_delivering_now','Has_Table_booking']].drop_duplicates()
    aux_df['Class']='Deliver and Booking'    
    aux_df.loc[((aux_df['Is_delivering_now']=='YES')&(aux_df['Has_Table_booking']=='NO')),'Class']='Only Deliver'                                   
    aux_df.loc[((aux_df['Is_delivering_now']=='NO')&(aux_df['Has_Table_booking']=='YES')),'Class']='Only Booking'
    aux_df.loc[((aux_df['Is_delivering_now']=='NO')&(aux_df['Has_Table_booking']=='NO')),'Class']='None'
    aux_df=aux_df.groupby(['Class']).count().reset_index()                                                                                                                                                                                                                                                                                         
    fig=pie(aux_df,names='Class',values='Restaurant_ID')
    return fig


def graph_priceRange(dados):
    from plotly.express import bar
    aux_df=dados[['Restaurant_ID','Average_Cost_for_two','Price_range','Has_Table_booking']].drop_duplicates()
    aux_df=aux_df.groupby(['Price_range'])[['Average_Cost_for_two']].mean().reset_index().sort_values(by='Average_Cost_for_two').round(2)                                                                                                                                                                                                                                                                                                                                                   
    fig=bar(aux_df,x='Price_range',y='Average_Cost_for_two',color='Price_range')
    return fig

def graph_priceRange_country(dados):
    from plotly.express import scatter
    aux_df=dados[['Country_name','Restaurant_ID','Average_Cost_for_two','Price_range','Has_Table_booking']].drop_duplicates()
    aux_df=aux_df.groupby(['Country_name','Price_range'])[['Average_Cost_for_two']].mean().reset_index().sort_values(by=['Country_name','Average_Cost_for_two']).round(2)                                                                                                                                                                                                                                                                                                                                                   
    fig=scatter(aux_df,x='Country_name',y='Price_range',size='Average_Cost_for_two',color='Price_range')
    return fig

#=======================================
#=======================================
#CITIES
#=======================================

def top_feature_city(dados,feature='Has_Table_booking'):

    aux_df=dados[['City','Restaurant_ID',feature]].drop_duplicates()    
    aux_df['restaurants']=1
    aux_df=aux_df.groupby(['City',feature])[['restaurants']].sum().reset_index()
    aux_df = aux_df.pivot(index='City', columns=feature, values='restaurants').fillna(0)
    aux_df=aux_df.sort_values(by='YES',ascending=False).reset_index()
    aux_df=aux_df[:10]

    aux_df=aux_df.rename(columns={'YES':'restaurants'})


    from plotly.express import bar
    fig=bar(aux_df,x='restaurants',y='City',orientation='h',color='City')
    fig.update_layout(showlegend=False)
    return fig

def top_cities_ratings(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['City','Restaurant_ID','Aggregate_rating']].drop_duplicates()
    aux_df['restaurants']=1
     
    bins = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    labels = ['0-0.5', '0.5-1', '1-1.5', '1.5-2', '2-2.5', '2.5-3', '3-3.5', '3.5-4', '4-4.5', '4.5-5']

    from pandas import cut
    aux_df['grupo'] = cut(aux_df['Aggregate_rating'], bins, labels=labels)
    aux_df=aux_df.groupby(['City','grupo'])[['restaurants']].sum().reset_index()
    aux_df=aux_df.pivot(index='City', columns='grupo', values='restaurants').reset_index()

    aux_df['TOP+4']=aux_df[['4-4.5', '4.5-5']].sum(axis=1)
    aux_df= aux_df.sort_values(by='TOP+4',ascending=False)
    aux_df['TOP+4']=range(1,len(aux_df)+1)

    aux_df['TOP-2.5']=aux_df[['0-0.5', '0.5-1', '1-1.5', '1.5-2', '2-2.5']].sum(axis=1)
    aux_df= aux_df.sort_values(by='TOP-2.5',ascending=False)
    aux_df['TOP-2.5']=range(1,len(aux_df)+1)


    top_4=aux_df[(aux_df['TOP+4']<=10)].sort_values(by='TOP+4')
    top_25=aux_df[(aux_df['TOP-2.5']<=10)].sort_values(by='TOP-2.5')

    top_4=top_4.drop(columns=['TOP+4','TOP-2.5']).reset_index(drop=True).set_index('City')
    top_25=top_25.drop(columns=['TOP+4','TOP-2.5']).reset_index(drop=True).set_index('City')

    return top_4,top_25

def Resume_city_info(dados):
    dados=dados.copy()

    def register_restaurant(dados):
        aux_df=dados[['Restaurant_ID','City']].drop_duplicates()
        aux_df=aux_df.groupby(['City']).count().rename(columns={'Restaurant_ID':'Restaurants'})
        return aux_df
    
    def cuisines_city(dados):
        aux_df=dados[['main_Cuisines','City']].drop_duplicates()
        aux_df=aux_df.groupby(['City']).count().rename(columns={'main_Cuisines':'Cuisines'})
        return aux_df
    
    def meal_cost_two(dados):
        aux_df=dados[['City','Restaurant_ID','Average_Cost_for_two']].drop_duplicates()
        aux_df=aux_df.groupby(['City'])[['Average_Cost_for_two']].mean().rename(columns={'Average_Cost_for_two':'mean_cost'})
        return aux_df
    
    def priceRange(dados,price_range='cheap'):
        aux_df=dados[['City','Restaurant_ID','Price_range']].drop_duplicates()
        aux_df=aux_df[aux_df['Price_range']==price_range]
        col=f'price_{price_range}'
        aux_df=aux_df.groupby(['City'])[['Price_range']].count().rename(columns={'Price_range':col})
        return aux_df[col]
    
    dataframe=[]

    dataframe.append(register_restaurant(dados))
    dataframe.append(cuisines_city(dados))
    dataframe.append(meal_cost_two(dados))   
    dataframe.append(priceRange(dados,price_range='cheap'))   
    dataframe.append(priceRange(dados,price_range='normal'))   
    dataframe.append(priceRange(dados,price_range='expensive'))   
    dataframe.append(priceRange(dados,price_range='gourmet'))   
    
    from pandas import concat
    resposta=concat(dataframe,axis=1).fillna(0)
    return resposta

def pie_priceRange(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Price_range','Restaurant_ID']].drop_duplicates()
    aux_df=aux_df.groupby(['Price_range']).count().reset_index().rename(columns={'Restaurant_ID':'Restaurants'})

    from plotly.express import pie
    color_map={
        'cheap':'green',
        'normal':'blue',
        'expensive':'yellow',
        'gourmet':'red'
    }

    fig=pie(aux_df,names='Price_range',values='Restaurants', color_discrete_map=color_map,color='Price_range')

    return fig
def mapa_folium(dados):
    aux_df=dados.copy()
    aux_df=aux_df[['Country_name','City','Longitude','Latitude','main_Cuisines','Restaurant_Name']].drop_duplicates()
    aux_df=aux_df
    #gerar mapa
    center_lon=aux_df['Longitude'].mean()
    center_lat=aux_df['Latitude'].mean()
    import folium
    from folium.plugins import MarkerCluster
    map = folium.Map(location=[center_lat, center_lon],zoom_start=2)

    marker_cluster = MarkerCluster().add_to(map)

    #colocar marcadores
    for restaurant in aux_df.index:
        lat,lon=aux_df.loc[restaurant,['Latitude','Longitude']]
        country,city,cuisine,name=aux_df.loc[restaurant,['Country_name','City','main_Cuisines','Restaurant_Name']]
        popup=f"""
        <h1><b>{name} </b></h1>
        <h3><b>Country: </b>{country}</h2> <br>
        <h3><b>City: </b>{city}</h2> <br>
        <h3><b>Cuisine: </b>{cuisine}</h2> <br>
            
            """
        popup=folium.Popup(popup, max_width=300)
    
        folium.Marker(
            location=[lat, lon],
            popup=popup,
            icon=folium.Icon(color="blue", icon="info-sign"),
        ).add_to(marker_cluster)

    
    return map
