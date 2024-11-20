財報分析及自動化交易平台

這是一個基於 Streamlit 的簡單應用程式，旨在提供股票財報分析和自動化交易的基礎功能。應用支援上傳財報文件、查看股票歷史價格趨勢，並結合 Python 和金融工具進行數據分析。

功能特點

	•	財報上傳與預覽：支持上傳 .csv 或 .xlsx 文件，並顯示內容預覽。
	•	股票數據下載：輸入股票代碼（如 AAPL 或 TSLA），自動抓取過去一年的歷史價格。
	•	價格走勢圖：根據股票數據繪製收盤價走勢圖。


如何運行？

1. 使用 Streamlit Cloud

如果已經部署到 Streamlit Cloud，你可以通過以下鏈接直接訪問應用程式：
點擊這裡訪問應用

2. 本地運行

如果你希望在本地運行，請按照以下步驟進行：
	1.	確保安裝了 Python 3.8 或以上版本。
	2.	克隆此專案：

git clone https://github.com/your-username/financeknowhow.git
cd financeknowhow

	3.	安裝依賴：
pip install -r requirements.txt

	4.	啟動應用：
streamlit run app.py



使用範例

1. 上傳財報

將 .csv 或 .xlsx 文件上傳到應用，然後應用將顯示數據的前幾行作為預覽。

2. 查看股票走勢

輸入股票代碼（如 AAPL），應用將自動抓取 Yahoo Finance 的歷史數據，並繪製出過去一年的收盤價走勢圖。

技術細節

	•	Python：應用使用 Python 的 pandas 和 yfinance 套件進行數據處理。
	•	Streamlit：作為應用的前端框架，實現交互式數據可視化。
