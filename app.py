import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🇩🇪 German Advertising Trends (2019–2024)")

df = pd.read_csv("data/ads_germany_1000.csv")

st.sidebar.header("Filters")
platform = st.sidebar.selectbox("Choose a Platform", ["All"] + df["Platform"].unique().tolist())
if platform != "All":
    df = df[df["Platform"] == platform]

st.subheader("Top Brands")
st.bar_chart(df["Brand"].value_counts().head(10))

st.subheader("Celebrity Appearances")
celeb_df = df[df["Celebrity Featured"] != ""]
st.bar_chart(celeb_df["Celebrity Featured"].value_counts().head(10))

st.subheader("Sample Ad Scripts")
st.dataframe(df[["Brand", "Ad Copy / Script"]].sample(5).reset_index(drop=True))
