import streamlit as st
import pandas as pd
import yfinance as yf

st.title("財報分析及自動化交易平台")

uploaded_file = st.file_uploader("上傳財報文件", type=["csv", "xlsx"])
if uploaded_file:
    data = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
    st.write("數據預覽：", data.head())

stock_ticker = st.text_input("輸入股票代碼 (e.g., AAPL, TSLA)")
if stock_ticker:
    stock_data = yf.download(stock_ticker, period="1y")
    st.line_chart(stock_data['Close']) 