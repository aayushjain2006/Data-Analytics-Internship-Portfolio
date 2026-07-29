import streamlit as st
import pandas as pd
import plotly.express as px

# Load Dataset

df = pd.read_excel("Data/superstore_cleaned.xlsx")

st.set_page_config(
    page_title="Superstore Dashboard",
    layout="wide"
)

st.title("📊 Superstore Deep-Dive Dashboard")

# Sidebar Filters

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

segment = st.sidebar.multiselect(
    "Select Segment",
    df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment))
]

# KPI Cards

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
avg_order = total_sales / total_orders

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Orders", total_orders)
col4.metric("Average Order", f"${avg_order:,.2f}")

st.divider()

# Sales by Region

sales_region = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig = px.bar(
    sales_region,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig, use_container_width=True)

# Sales by Category

sales_category = filtered_df.groupby("Category")["Sales"].sum().reset_index()

fig = px.pie(
    sales_category,
    names="Category",
    values="Sales",
    title="Sales by Category"
)

st.plotly_chart(fig, use_container_width=True)


# Monthly Sales

filtered_df["Order Date"] = pd.to_datetime(filtered_df["Order Date"])

filtered_df["Month"] = filtered_df["Order Date"].dt.strftime("%Y-%m")

monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()

fig = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig, use_container_width=True)

# Top Customers

top_customers = filtered_df.groupby("Customer Name")["Sales"].sum().nlargest(10).reset_index()

fig = px.bar(
    top_customers,
    x="Customer Name",
    y="Sales",
    title="Top 10 Customers"
)

st.plotly_chart(fig, use_container_width=True)

# Profit by Sub-Category

subcategory = filtered_df.groupby("Sub-Category")["Profit"].sum().reset_index()

fig = px.bar(
    subcategory,
    x="Sub-Category",
    y="Profit",
    title="Profit by Sub-Category"
)

st.plotly_chart(fig, use_container_width=True)