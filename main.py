import yfinance as yf
import streamlit as st
from urllib.request import urlopen
from PIL import Image

#vARIABLE
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = 'XRP-USD'
BitcoinCash = 'BCH-USD'

#Title and Subtitle
st.title("Cryptocurrency Daily Prices")
st.subheader('Preços diários de criptomoedas')
st.header("(Main Dashboard) " + "Painel Principal")
st.subheader("you can add more crypto in cod")

#Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)

#Fetch history data from yahoo Finance
BTCHHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")

#Fetch crypto data for the dataframe
BTC = yf.download(Bitcoin, start="2021-11-18",
                  end='2022-03-06').tail(1)
ETH = yf.download(Ethereum, start="2021-11-18",
                  end='2022-03-06').tail(1)
XRP = yf.download(Ripple, start="2021-11-18",
                  end='2022-03-06').tail(1)
BCH = yf.download(BitcoinCash, start="2021-11-18",
                  end='2022-03-06').tail(1)
#Bitcoin
st.write('BITCOIN ($)')
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
#Display image
st.image(imageBTC)
#Display dataframe
st.table(BTC)
#Display a chart
st.bar_chart(BTCHHis.Close)

#Ethereum
st.write('ETHEREUM ($)')
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
#Display image
st.image(imageETH)
#Display dataframe
st.table(ETH)
#Display a chart
st.line_chart(ETHHis.Close)

#Riplle
st.write('RIPLLE ($)')
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
#Display image
st.image(imageXRP)
#Display dataframe
st.table(XRP)
#Display a chart
st.bar_chart(XRPHis.Close)

#Bitcoin Cash
st.write('BITCOIN  CASH ($)')
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
#Display image
st.image(imageBCH)
#Display dataframe
st.table(BCH)
#Display a chart
st.line_chart(BCHHis.Close)