def barra_lateral_padrao(data,st):

    #HEADER

    #st.sidebar.image('./imagens/logo.png',width=120)
    st.sidebar.markdown('# FOME ZERO')
    st.sidebar.markdown('## Nosso negócio é matar a sua fome.')
    st.sidebar.markdown("""---""")

    #FILTROS

    opcoes=['YES', 'NO']
    Has_Table_booking=st.sidebar.multiselect('Accept Booking',opcoes,default=opcoes)

    opcoes=['YES', 'NO']
    Is_delivering_now=st.sidebar.multiselect('Is delivering',opcoes,default=opcoes)

    opcoes=['YES', 'NO']
    Has_Online_delivery=st.sidebar.multiselect('Accept online orders',opcoes,default=opcoes)


    opcoes=['expensive', 'gourmet', 'normal', 'cheap']
    Price_range=st.sidebar.multiselect('Price Range',opcoes,default=opcoes)

    opcoes=['Philippines', 'Brazil', 'Australia', 'United States of America',
        'Canada', 'Singapure', 'United Arab Emirates', 'India',
        'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
        'Sri Lanka', 'Turkey']
    Country_name=st.sidebar.multiselect('Country',opcoes,default=opcoes)

    st.sidebar.markdown("""---""")

    #APLICAR FILTROS
    filtro_linhas=((data['Has_Table_booking'].isin(Has_Table_booking))&
                (data['Is_delivering_now'].isin(Is_delivering_now))&
                (data['Has_Online_delivery'].isin(Has_Online_delivery))&
                (data['Price_range'].isin(Price_range))&
                (data['Country_name'].isin(Country_name))
                )
    data=data.loc[filtro_linhas,:]
    return data