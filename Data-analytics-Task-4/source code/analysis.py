import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from scipy.stats import ttest_ind

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)

print("=" * 50)
print("SUPERSTORE DATA ANALYSIS PROJECT")
print("=" * 50)

df = pd.read_excel("Data/superstore_cleaned.xlsx")
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
print(df["Order Date"].head())
print(df["Order Date"].dtype)

print("\n Dataset Loaded Successfully!")

print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())


print("\n========== DATASET SHAPE ==========\n")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\n========== COLUMN NAMES ==========\n")
print(df.columns.tolist())


print("\n========== DATASET INFORMATION ==========\n")
df.info()


print("\n========== STATISTICAL SUMMARY ==========\n")
print(df.describe())


print("\n========== MISSING VALUES ==========\n")
print(df.isnull().sum())


print("\n========== DUPLICATE RECORDS ==========\n")
print("Duplicate Rows :", df.duplicated().sum())


import os
os.makedirs("image", exist_ok=True)

sales_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))

sales_region.plot(
    kind="bar",
    color=["royalblue","orange","green","red"]
)

plt.title("Total Sales by Region", fontsize=15)
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)

plt.savefig("image/sales_by_region.png", dpi=300, bbox_inches="tight")

plt.show()

print(" sales_by_region.png saved successfully")

profit_category = (
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))

bars = plt.bar(
    profit_category.index,
    profit_category.values,
    color=["#2ECC71", "#3498DB", "#E74C3C"]
)

plt.title("Total Profit by Category", fontsize=16, fontweight="bold")
plt.xlabel("Category", fontsize=12)
plt.ylabel("Profit", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)


for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()

plt.savefig("image/profit_by_category.png", dpi=300)

plt.show()

print(" profit_by_category.png saved successfully")


segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8,8))

colors = ["#3498DB", "#2ECC71", "#F39C12"]

plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    shadow=True,
    explode=(0.03,0.03,0.03)
)

plt.title("Sales Distribution by Segment", fontsize=16, fontweight="bold")

plt.savefig("image/sales_by_segment.png", dpi=300)

plt.show()

print("sales_by_segment.png saved successfully")


df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(15,6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=90)

plt.grid(True)

plt.tight_layout()

plt.savefig("image/monthly_sales_trend.png", dpi=300)

plt.show()

print(" monthly_sales_trend.png saved successfully")

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

bars = plt.barh(
    top_products.index,
    top_products.values,
    color="steelblue"
)

plt.title("Top 10 Products by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.gca().invert_yaxis()

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y()+bar.get_height()/2,
        f"{bar.get_width():,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig("image/top_10_products.png", dpi=300)

plt.show()

print(" top_10_products.png saved successfully")


top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))

bars = plt.barh(
    top_customers.index,
    top_customers.values,
    color="darkorange"
)

plt.title("Top 10 Customers by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Sales")
plt.ylabel("Customer")

plt.gca().invert_yaxis()

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y()+bar.get_height()/2,
        f"{bar.get_width():,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig("image/top_10_customers.png", dpi=300)

plt.show()

print("top_10_customers.png saved successfully")


plt.figure(figsize=(10,6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.6,
    color="purple"
)

plt.title("Discount vs Profit", fontsize=16, fontweight="bold")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()

plt.savefig("image/discount_vs_profit.png", dpi=300)

plt.show()

print("discount_vs_profit.png saved successfully")

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap", fontsize=16, fontweight="bold")

plt.tight_layout()

plt.savefig("image/correlation_heatmap.png", dpi=300)

plt.show()

print("correlation_heatmap.png saved successfully")

ship_sales = (
    df.groupby("Ship Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(9,5))

bars = plt.bar(
    ship_sales.index,
    ship_sales.values,
    color="teal"
)

plt.title("Sales by Ship Mode", fontsize=16, fontweight="bold")
plt.xlabel("Ship Mode")
plt.ylabel("Sales")

plt.xticks(rotation=20)

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig("image/sales_by_ship_mode.png", dpi=300)

plt.show()

print("sales_by_ship_mode.png saved successfully")

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))

bars = plt.barh(
    top_states.index,
    top_states.values,
    color="darkcyan"
)

plt.title("Top 10 States by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Sales")
plt.ylabel("State")

plt.gca().invert_yaxis()

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y()+bar.get_height()/2,
        f"{bar.get_width():,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig("image/top_10_states.png", dpi=300)

plt.show()

print("top_10_states.png saved successfully")


print("\n" + "="*60)
print("BUSINESS INSIGHTS")
print("="*60)

top_region = df.groupby("Region")["Sales"].sum().idxmax()
print(f"1. Region with Highest Sales : {top_region}")

top_category = df.groupby("Category")["Profit"].sum().idxmax()
print(f"2. Most Profitable Category : {top_category}")

top_segment = df.groupby("Segment")["Sales"].sum().idxmax()
print(f"3. Segment with Highest Sales : {top_segment}")

top_ship = df["Ship Mode"].mode()[0]
print(f"4. Most Used Shipping Mode : {top_ship}")

top_state = df.groupby("State")["Sales"].sum().idxmax()
print(f"5. State with Highest Sales : {top_state}")

top_customer = df.groupby("Customer Name")["Sales"].sum().idxmax()
print(f"6. Top Customer : {top_customer}")

top_product = df.groupby("Product Name")["Sales"].sum().idxmax()
print(f"7. Top Selling Product : {top_product}")

print(f"8. Average Discount : {df['Discount'].mean():.2f}")

print(f"9. Average Profit : {df['Profit'].mean():.2f}")

print(f"10. Total Sales : {df['Sales'].sum():,.2f}")

print("\n" + "=" * 60)
print("HYPOTHESIS TESTING")
print("=" * 60)

technology_profit = df[df["Category"] == "Technology"]["Profit"]
furniture_profit = df[df["Category"] == "Furniture"]["Profit"]
t_statistic, p_value = ttest_ind(
    technology_profit,
    furniture_profit,
    equal_var=False
)

print(f"T-Statistic : {t_statistic:.4f}")
print(f"P-Value     : {p_value:.6f}")

alpha = 0.05

if p_value < alpha:
    print("\nDecision : Reject the Null Hypothesis (H0)")
    print("Conclusion : Technology products have a statistically significant difference in average profit compared with Furniture products.")
else:
    print("\nDecision : Fail to Reject the Null Hypothesis (H0)")
    print("Conclusion : There is no statistically significant difference in average profit between Technology and Furniture products.")