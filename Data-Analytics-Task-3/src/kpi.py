def calculate_kpis(df):

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_orders = df["Order ID"].nunique()

    average_order_value = total_sales / total_orders

    profit_margin = (total_profit / total_sales) * 100

    return {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Total Orders": total_orders,
        "Average Order Value": average_order_value,
        "Profit Margin": profit_margin
    }