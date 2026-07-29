import pandas as pd

def sales_by_region(df):
    return df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

def sales_by_category(df):
    return df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

def sales_by_segment(df):
    return df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

def profit_by_category(df):
    return df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

def top_10_customers(df):
    return df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

def top_10_products(df):
    return df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

def monthly_sales(df):
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

    return df.groupby("Month")["Sales"].sum()

def customer_segmentation(df):
    customer_sales = df.groupby("Customer Name")["Sales"].sum()

    def segment(sales):
        if sales >= 5000:
            return "High Value"
        elif sales >= 1000:
            return "Medium Value"
        else:
            return "Low Value"

    segmentation = customer_sales.apply(segment)

    return segmentation.value_counts()

def state_wise_sales(df):
    return df.groupby("State")["Sales"].sum().sort_values(ascending=False)

def subcategory_profit(df):
    return df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False)