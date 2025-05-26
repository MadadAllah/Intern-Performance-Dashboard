import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Intern Performance Dashboard", layout="wide")

# Load your CSV
df = pd.read_csv("Cleaned_Intern_Performance_Data.csv", parse_dates=["Date of Assignment", "Date of Completion"])

# Title
st.title("📊 Intern Performance Evaluation Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")
selected_depts = st.sidebar.multiselect("Department", df["Department"].unique(), default=df["Department"].unique())
selected_status = st.sidebar.multiselect("Status", df["Completion_Status"].unique(), default=df["Completion_Status"].unique())

df = df[(df["Department"].isin(selected_depts)) & (df["Completion_Status"].isin(selected_status))]

# KPIs
st.subheader("📈 Key Performance Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Completion Days", f"{df['Task_Completion_Days'].mean():.2f}")
col2.metric("Avg Quality Score", f"{df['Project_Quality_Score'].mean():.2f}")
col3.metric("Avg Feedback Score", f"{df['Mentor_Feedback_Score'].mean():.2f}")

# Chart 1: Completion Time Distribution
st.subheader("⏳ Task Completion Time Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df['Task_Completion_Days'].dropna(), bins=30, ax=ax1, color='skyblue')
st.pyplot(fig1)

# Chart 2: Quality by Department
st.subheader("📋 Average Project Quality by Department")
fig2, ax2 = plt.subplots()
df.groupby("Department")["Project_Quality_Score"].mean().plot(kind='barh', ax=ax2, color='mediumseagreen')
st.pyplot(fig2)

# Chart 3: Feedback by Department
st.subheader("💬 Average Mentor Feedback by Department")
fig3, ax3 = plt.subplots()
df.groupby("Department")["Mentor_Feedback_Score"].mean().plot(kind='barh', ax=ax3, color='salmon')
st.pyplot(fig3)
