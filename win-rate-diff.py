import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Drop missing values
df = df.dropna(subset=["opening_name", "winner_color"])

# 🎯 Identify popular openings (with >100 games)
popular_openings = df["opening_name"].value_counts()
popular_openings = popular_openings[popular_openings > 10000].index

# 📌 Filter dataset for only popular openings
df_popular = df[df["opening_name"].isin(popular_openings)]

# 🧮 Count white and black wins for each opening
opening_stats = df_popular.groupby("opening_name")["winner_color"].value_counts().unstack().fillna(0)

# Total games per opening
opening_stats["total"] = opening_stats.sum(axis=1)

# Calculate win rates
opening_stats["white_win_rate"] = opening_stats["White"] / opening_stats["total"]
opening_stats["black_win_rate"] = opening_stats["Black"] / opening_stats["total"]

# Calculate win rate difference
opening_stats["win_rate_diff"] = opening_stats["white_win_rate"] - opening_stats["black_win_rate"]

# Sort by win rate difference
opening_stats_sorted = opening_stats.sort_values("win_rate_diff", ascending=False)

# 📊 Plot the bar chart
plt.figure(figsize=(14, 7))
opening_stats_sorted["win_rate_diff"].plot(kind="bar", color="mediumseagreen", edgecolor="black")

plt.title("Win Rate Difference (White - Black) for Popular Openings (>1000 games)")
plt.xlabel("Opening Name")
plt.ylabel("Win Rate Difference")
plt.axhline(0, color="gray", linestyle="--")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
