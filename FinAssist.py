import streamlit as st
import requests
import time

# API Keys
HUGGINGFACE_API_KEY = "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"
ALPHA_VANTAGE_API_KEY = "7XUKEM8OXSI0UEJT"
FINANCIAL_MODEL = "Qwen/Qwen2.5-Coder-32B-Instruct"
PRODUCT_RECOMMENDATION_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"

def call_huggingface(model, prompt, retries=3, delay=5, token_limit=4000):
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": token_limit}}
    
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                json_response = response.json()
                if isinstance(json_response, list) and "generated_text" in json_response[0]:
                    return json_response[0]["generated_text"]
                return "⚠️ Unexpected API response format."
            elif response.status_code == 503:
                time.sleep(delay)
            else:
                return f"API Error: {response.status_code} - {response.json()}"
        except Exception as e:
            return f"API Error: {e}"
    return "⚠️ Service Unavailable. Please try again later."

def get_stock_data(stock_symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url).json()
    
    if "Time Series (5min)" not in response:
        return None, "Invalid stock symbol or API limit reached."
    
    time_series = response["Time Series (5min)"]
    times, prices = zip(*[(t, float(data["1. open"])) for t, data in sorted(time_series.items())])
    
    return (times, prices), f"Latest Price of {stock_symbol}: ${prices[-1]}"

# Streamlit UI
st.set_page_config(page_title="GenAI Financial Assistant", layout="wide")
st.title("💰 GenAI Financial Assistant")

# Financial Advice
st.header("📢 Financial Advice")
prompt_text = st.text_area("Ask your financial question or describe your investment needs:")
if st.button("Get Financial Advice"):
    if prompt_text.strip():
        financial_advice = call_huggingface(FINANCIAL_MODEL, prompt_text)
        product_recommendations = call_huggingface(PRODUCT_RECOMMENDATION_MODEL, f"Based on the following financial advice, recommend investment products: {financial_advice}")
        st.subheader("Financial Advice:")
        st.write(financial_advice)
        st.subheader("Recommended Investment Products:")
        st.write(product_recommendations)
    else:
        st.warning("Please enter a question.")

# Stock Market Data
st.header("📈 Stock Market Data")
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, INFY.BSE):")
if st.button("Get Stock Price & Graph"):
    if stock_symbol.strip():
        (times, prices), message = get_stock_data(stock_symbol)
        st.write(message)
    else:
        st.warning("Please enter a stock symbol.")

# Risk Profiling Quiz
st.header("🎯 Risk Profiling")
risk_level = st.selectbox("Select your risk tolerance:", ["Low", "Medium", "High"])
if st.button("Get Investment Suggestions"):
    advice = call_huggingface(PRODUCT_RECOMMENDATION_MODEL, f"Suggest investment options for someone with {risk_level} risk tolerance.")
    st.subheader(f"Investment Suggestions for {risk_level} Risk:")
    st.write(advice)

# Dark Mode Toggle
if st.checkbox("🌙 Enable Dark Mode"):
    st.markdown(
        """
        <style>
            body {
                background-color: #121212;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )