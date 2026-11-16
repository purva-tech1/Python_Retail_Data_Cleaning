import pandas as pd

# 1. Load raw retail dataset
df = pd.read_csv("retail_sales_raw.csv")

# 2. Inspect dataset structure and missing values
print("Dataset Shape:", df.shape)
print("Missing Values:\n", df.isnull().sum())

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Handle missing values safely
df["sales_amount"] = df["sales_amount"].fillna(df["sales_amount"].median())
df["city"] = df["city"].fillna("Unknown")
df = df.dropna(subset=["order_id", "order_date"])

# 5. Standardize text formatting and date column
df["category"] = df["category"].str.strip().str.title()
df["order_date"] = pd.to_datetime(df["order_date"])

# 6. Summarize total revenue and average order value by category
category_summary = (
    df.groupby("category")["sales_amount"]
    .agg(total_revenue="sum", avg_order_value="mean", order_count="count")
    .reset_index()
    .sort_values(by="total_revenue", ascending=False)
)

print("\nCategory Performance Summary:\n", category_summary)

# 7. Export cleaned dataset
df.to_csv("retail_sales_cleaned.csv", index=False)
