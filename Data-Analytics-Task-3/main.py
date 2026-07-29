from src.utils import load_data
from src.kpi import calculate_kpis
from src.analysis import *
from src.charts import *
 
df = load_data()

# ---------------- KPIs ----------------
kpis = calculate_kpis(df)

print("=" * 50)
print("SUPERSTORE KPI REPORT")
print("=" * 50)

for key, value in kpis.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")

# ---------------- Analysis ----------------
region_sales = sales_by_region(df)
category_sales = sales_by_category(df)
segment_sales = sales_by_segment(df)
category_profit = profit_by_category(df)
top_customers = top_10_customers(df)
top_products = top_10_products(df)
monthly = monthly_sales(df)
customer_segment = customer_segmentation(df)
state_sales = state_wise_sales(df)
subcategory = subcategory_profit(df)

# ---------------- Charts ----------------
save_bar_chart(region_sales,
               "Sales by Region",
               "Region",
               "Sales",
               "sales_region.png")

save_bar_chart(category_sales,
               "Sales by Category",
               "Category",
               "Sales",
               "sales_category.png")

save_bar_chart(category_profit,
               "Profit by Category",
               "Category",
               "Profit",
               "profit_category.png")

save_bar_chart(top_customers,
               "Top 10 Customers",
               "Customer",
               "Sales",
               "top_customers.png")

save_bar_chart(top_products,
               "Top 10 Products",
               "Product",
               "Sales",
               "top_products.png")

save_line_chart(monthly,
                "Monthly Sales Trend",
                "Month",
                "Sales",
                "monthly_sales.png")

save_pie_chart(customer_segment,
               "Customer Segmentation",
               "customer_segmentation.png")

save_bar_chart(state_sales,
               "Sales by State",
               "State",
               "Sales",
               "state_sales.png")

save_bar_chart(subcategory,
               "Profit by Sub Category",
               "Sub Category",
               "Profit",
               "subcategory_profit.png")

print("\nCharts Generated Successfully!")
print("Location: output/charts/")