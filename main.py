import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.write("""
# Web response
График web_response
""")

df = pd.read_csv("web_response.csv")
df['point'] = df['point'].astype('datetime64[ns]')
df = df[:1000]

st.line_chart(
   df, x="point", y=["web_response"], color=["#0800ff"]  # Optional
)

st.write("""
# Throughput
График throughput
""")

df = pd.read_csv("throughput.csv")
df['point'] = df['point'].astype('datetime64[ns]')
df = df[:10060]

st.line_chart(
   df, x="point", y=["call_count"], color=["#00ff2a"]  # Optional
)


st.write("""
# Apdex
График apdex
""")

df = pd.read_csv("apdex.csv")
df['point'] = df['point'].astype('datetime64[ns]')
df = df[:1000]

st.line_chart(
   df, x="point", y=["apdex"], color=["#8700ff"]  # Optional
)


st.write("""
# Error
График error
""")

df_2 = pd.read_csv("error.csv")
print(df_2)
df_2['point'] = df_2['point'].astype('datetime64[ns]')
df_2 = df_2[:1000]

st.line_chart(
   df_2, x="point", y=["call_count"], color=["#FF0000"]  # Optional
)