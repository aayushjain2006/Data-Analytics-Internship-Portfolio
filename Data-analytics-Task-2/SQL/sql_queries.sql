Q1. Top 5 Products by Sales
SELECT Product_Name, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 5;


Q2. Region with Highest Sales
SELECT Region, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;


Q3. Category-wise Profit
SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category;


Q4. Top Customers
SELECT Customer_Name, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;


Q5. Average Discount by Category
SELECT Category, AVG(Discount) AS Avg_Discount
FROM superstore
GROUP BY Category;
