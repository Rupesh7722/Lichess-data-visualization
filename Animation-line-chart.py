import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Convert date and get month
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# Remove rows without opening names
df = df.dropna(subset=["opening_name"])

# Find top 10 openings
top_openings = df["opening_name"].value_counts().nlargest(10).index

# Filter for top openings
df_top = df[df["opening_name"].isin(top_openings)]

# Count games for each month and opening
counts = df_top.groupby(["month", "opening_name"]).size().unstack(fill_value=0)

# Plot directly
counts.plot(kind="line", marker="o", figsize=(12, 6))
plt.title("Top 10 Chess Openings Popularity Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Games")
plt.show()
