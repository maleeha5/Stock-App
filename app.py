import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf


st.write("""
### Stock Price App

###### Select the start date and the end date from the side bar to load the line charts for the companies
###### Select one or multiple actions to display plots for the desired action

""")

startt = st.sidebar.date_input('Select the start date')

endd = st.sidebar.date_input('Select the end date')



stocks = ['AAPL','GOOGL','MSFT','FB']

list = ['Open','High','Close','Volume','Dividends']
option = st.sidebar.multiselect('Choose the column to be displayed option',list)

def create_plots(stocks):
    for stock in stocks:
        tickerSymbol = stock
        tickerData = yf.Ticker(tickerSymbol)
        tickerDf = tickerData.history(period ='5d', start=startt, end=endd)
        


       
        #st.write(option)     
        
        for word in option :
            st.write('Shown are the',word, 'stocks of ',stock)
            if word == 'Open':
                st.line_chart(tickerDf.Open)
            if word == 'High':
                st.line_chart(tickerDf.High)
            if word == 'Close':
                st.line_chart(tickerDf.Close)
            if word == 'Volume':
                st.line_chart(tickerDf.Volume)
            if word == 'Dividends':
                st.line_chart(tickerDf.Dividends)


create_plots(stocks)