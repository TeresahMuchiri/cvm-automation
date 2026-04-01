import streamlit as st
import pandas as pd

st.title("CVM Campaign Dashboard")

df = pd.read_csv('data/campaign_results.csv')

st.subheader("Customer Data")
st.write(df)

total = len(df)

open_rate = df['opened'].sum() / total
click_rate = df['clicked'].sum() / total
conversion_rate = df['converted'].sum() / total

st.subheader("Metrics")
st.write(f"Open Rate: {open_rate:.2f}")
st.write(f"Click Rate: {click_rate:.2f}")
st.write(f"Conversion Rate: {conversion_rate:.2f}")

st.subheader("Conversions")
st.bar_chart(df['converted'].value_counts())