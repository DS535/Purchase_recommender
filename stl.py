import streamlit as st
import pandas as pd
import numpy as np
import turicreate as tc
import pickle
import webbrowser
import streamlit.components.v1 as components



rad=st.sidebar.radio("Navigation",["Home", "Trends","User Similarity Recommendation"])

if rad=="Trends":
    st.title('Brand Trends')
    df = pd.read_csv('filterData.csv')
    for idx in range(df.shape[0]):
        df.loc[idx,"OnlyDate"] = df.Date.str.split(" ")[idx][0]
    def week():
        dates = ['2021-04-'+str(num) for num in range(12,20)]
        return dates
    def month():
        dates = ['2021-03-'+str(num) for num in range(1,30)]
        return dates
    def halfYear():
        dates = ['2021-03-'+str(num) for num in range(1,30)]
        return dates
    def yearly():
        st.write('6 Months')
        selectedCustomerDf = df[df.Customer_id == customer_id]
        brandTrends = selectedCustomerDf[selectedCustomerDf.OnlyDate.str.contains('04') | selectedCustomerDf.OnlyDate.str.contains('01') | selectedCustomerDf.OnlyDate.str.contains('02')].Brand.value_counts()
        st.bar_chart(brandTrends[:5])
    def monthly():
        st.write('1 month')
        dates = month()
        selectedCustomerDf = df[df.Customer_id == customer_id]
        brandTrends = selectedCustomerDf[selectedCustomerDf.OnlyDate.str.contains('04')].Brand.value_counts()
        st.bar_chart(brandTrends[:5])
    customer_id = st.selectbox(
         'Customers',
         df.Customer_id.unique())
    st.write('You selected:', customer_id)
    # if st.button('6 Months Trends'):
    yearly()
    # if st.button('Monthly Trends'):
    monthly()


if rad=="Customer Segmentation":
    st.header("Types of Customer Purchase Behaviour")
    st.image("cust_behave.png")
    st.header("****DOSH Behavioral Data Integration can further improve the efficiency and relevancy of these segments***")
    
if rad=="Home":
    st.header("Team : Mission Impossible") 
    st.title('Purchase Behavior Prediction Model')
    st.image("rec.png")
    st.header("Business Opportunity :")
    st.subheader("Personalized offers/promotions will certainly have higher success rate in increasing Customer's interest levels to activate and utilize them")
    st.text("")
    st.header("Analytical Scope: ")
    st.subheader("Developing customized models which can understand inherent geo-based purchase behaviour of individual customers and create purchase behaviour oriented personas")
    st.text("")
    st.text("")
    st.header("Data Sources: Purchase Graph-MLC Model")

    def load_data():
        data=pd.read_csv("data_500.csv")
        return data

    data=load_data()

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        
        
    
    #user_input = st.text_input("Enter a Customer ID to see The Recommendation")
        st.header("Top Trending Brands in the City")
        st.write(data[:10])
        
        
    url = 'file:///C:/Users/dsingh/Desktop/VADER/Hackathon/MapBox.html'

    if st.button('Geographical Representation of Purchase Behaviour'):
        webbrowser.open_new_tab(url)
      




    #st. image("https://media.giphy.com/media/3ohzdIuqJoo8QdKlnW/giphy.gif")
    cu=st.text_input("Enter a Customer ID to see The top purchase history")
   
    customer_data=data[data["Customer_id"]==cu]["Brand"].value_counts()
    st.bar_chart(customer_data[0:5])
    
if rad=="User Similarity Recommendation":
    st.header('Recommendations based on User Similarity')
    

    final_model = tc.load_model('recommender.h5')

    with open("brand_dict_reverse.pkl","rb") as rd:
        rest_dict=pickle.load(rd)

    def pred_results(k):
        uid = st.text_input("Enter a Customer ID to see The Recommendation")
        recom = final_model.recommend(users=[uid], k=k)
        recom = recom.to_dataframe() # convertinng sframe to dataframe
        product_list=recom["productId"]
        predictions=[rest_dict[i] for i in product_list]
        for element in predictions:
            st.text(element)
        return predictions

    pred_results(10)


