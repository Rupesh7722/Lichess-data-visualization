import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Prepare month column
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# Remove missing values
df = df.dropna(subset=["opening_name", "winner_color"])

# Top 5 openings (keep it small & simple)
top_openings = df["opening_name"].value_counts().nlargest(5).index
df = df[df["opening_name"].isin(top_openings)]

# Calculate white win rate per month & opening
summary = (
    df.assign(white_win=(df["winner_color"].str.lower() == "white").astype(int))
      .groupby(["opening_name", "month"])["white_win"]
      .mean()
      .reset_index()
)

# Convert to percentage
summary["white_win_rate"] = summary["white_win"] * 100

# Simple line plot
fig = px.line(
    summary,
    x="month",
    y="white_win_rate",
    color="opening_name",
    markers=True,
    title="White Win Rate Trends (Top 5 Openings)"
)
fig.show()
