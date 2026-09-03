import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Order_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,
                 1011,1012,1013,1014,1015,1016,1017,1018,1019,1020],
    
    "Customer": ["Amit","Riya","Sneha","Karan","Amit","Priya","Riya","Sneha",
                 "Karan","Amit","Priya","Riya","Karan","Sneha","Amit","Priya",
                 "Riya","Karan","Sneha","Amit"],
    
    "Region": ["East","West","East","North","East","South","West","East",
               "North","East","South","West","North","East","East","South",
               "West","North","East","East"],
    
    "Category": ["Electronics","Furniture","Accessories","Electronics","Furniture",
                 "Accessories","Electronics","Furniture","Accessories","Electronics",
                 "Furniture","Accessories","Electronics","Accessories","Furniture",
                 "Electronics","Furniture","Accessories","Electronics","Furniture"],
    
    "Sales": [60000,45000,22000,70000,38000,18000,52000,48000,25000,65000,
              42000,15000,58000,20000,50000,55000,47000,28000,62000,53000],
    
    "Profit": [12000,9000,5000,15000,8000,4000,11000,10000,5500,13000,
               8500,3000,12000,4500,10000,11000,9500,6000,12500,10500]
})
print("\n===== Phase 1 : Data Understanding =====")
print("\n---- Task 1 : Displaying Dataframe ----")
print(df)

print("\n---- Task 2 : Basic Analysis ----")
print("Count of Unique Customers", df["Customer"] .nunique())
print("Number of Regions", df["Region"] .nunique())
print("Number of Categories", df["Category"] .nunique())
print("Frequency of Each Category", df["Category"] .value_counts())

print("\n---- Task 3 : Checking Duplicates ----")
print("No. Duplicates by Order_ID:", df.duplicated("Order_ID") .sum())

print("\n===== Phase 2 & Task 4 : Business KPIs =====")
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
print("Overall Profit Margin:", (df["Profit"].sum() / df["Sales"].sum())*100 )

print("\n===== Phase 3 : Regional Analysis =====")
print("\n---- Task 5 : Regional Summary ----")
region_summary= df.groupby("Region") .agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Sales=("Sales", "mean")
) 
print(region_summary .sort_values(by="Total_Sales", ascending=False))

print("\n---- Task 6 : Best Performing Region(s) ----")
print("Highest-Sales Region:", region_summary["Total_Sales"] .sort_values() .tail(1))
print("Highest-profit Region:", region_summary["Total_Profit"] .idxmax())

print("\n===== Phase 4 : Category Analysis =====")
print("\n---- Task 7 : Category Overview ----")
category_summary= df.groupby("Category") .agg(Total_Sales=("Sales", "sum"),
                                      Total_Profit=("Profit", "sum")) 
print(category_summary.sort_values(by="Total_Profit", ascending=False))

print("\n---- Task 8 : Category vs Region Matrix ----")
Matrix= pd.pivot_table(df,
                       index="Region",
                       columns="Category",
                       values="Sales",
                       aggfunc="sum")
print(Matrix)

print("\n===== Phase 5 : Customer Analysis =====")
print("\n---- Task 9 : Customer Summary ----")
customer_summary= df.groupby("Customer") .agg(Total_Sales= ("Sales", "sum"),
                                              Total_Profit=("Profit", "sum"),
                                              Average_Sales=("Sales", "mean"))
print(customer_summary .sort_values(by="Total_Sales", ascending=False))

print("\n---- Task 10 : Customer Contributing to Highest Profit ----")
print("Highest Total Profit Contributor:", customer_summary["Total_Profit"] .idxmax())

print("\n===== Phase 6 : Visualization =====")
print("\n---- Task 11 : Sales By Region Bar Chart ----")
plt.bar(region_summary.index, region_summary["Total_Sales"], color="skyblue")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()

print("\n---- Task 12 : Sales Sequence through Line Chart ----")
plt.plot(df["Sales"], color="orange")
plt.title("Sales Sequence")
plt.xlabel("Frequency")
plt.ylabel("Sales")

plt.show()

print("\n---- Task 13 : Sales Vs Profit (Scatter Plot) ----")
plt.figure(figsize=(6,4))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales and Profit Comparison")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

print("\n===== Phase 7 : Export Data =====")
print("\n---- Task 14 : Exporting Summaries ----")
region_summary.to_excel("Regional_Summary.xlsx")
category_summary.to_excel("Category_Summary.xlsx")
customer_summary.to_excel("Customer_Summary.xlsx")

print(pd.read_excel("Regional_Summary.xlsx"))
print(pd.read_excel("Category_Summary.xlsx"))
print(pd.read_excel("Customer_Summary.xlsx"))