import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Convert date and extract month
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# Drop rows missing opening names
df = df.dropna(subset=["opening_name"])

# Get top 10 openings (minor edit: documented reasoning)
top_openings = df["opening_name"].value_counts().nlargest(10).index

# Filter dataset
df_top = df[df["opening_name"].isin(top_openings)]

# Count games per opening per month
counts = df_top.groupby(["month", "opening_name"]).size().unstack(fill_value=0)

# Minor edit: sort openings alphabetically for consistent plotting
counts = counts.reindex(sorted(counts.columns), axis=1)

# Plot
counts.plot(kind="line", marker="o", figsize=(12, 6))
plt.title("Top 10 Chess Openings Popularity Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Games")
plt.tight_layout()
plt.show()
