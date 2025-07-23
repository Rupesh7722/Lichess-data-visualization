import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("lichess_merged_7months.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# Normalize winner_color capitalization
df["winner_color"] = df["winner_color"].str.lower()

# Drop missing values
df = df.dropna(subset=["opening_name", "winner_color", "white_rating", "black_rating"])

# Get Top 10 Openings
top_openings = df["opening_name"].value_counts().nlargest(10).index.tolist()

# Filter dataset to include only top 10 openings
df_top = df[df["opening_name"].isin(top_openings)].copy()

# Calculate white win flag
df_top["white_win_flag"] = df_top["winner_color"].apply(
    lambda x: 1 if x == "white" else (0 if x == "black" else None)
)

# Filter valid games
df_top = df_top[df_top["white_win_flag"].isin([0, 1])]

# Group by opening and month
summary = df_top.groupby(["opening_name", "month"]).agg(
    white_win_rate=("white_win_flag", "mean"),
    avg_elo=("white_rating", "mean"),
    game_count=("white_win_flag", "count")
).reset_index()

# Convert to percent
summary["white_win_rate_percent"] = summary["white_win_rate"] * 100

# 🧠 Plot using facet (subplot for each opening)
fig = px.line(
    summary,
    x="month",
    y="white_win_rate_percent",
    facet_col="opening_name",
    facet_col_wrap=2,  # 2 columns per row
    title="📊 White Win Rate Trends for Top 10 Chess Openings",
    markers=True,
    category_orders={"month": sorted(df["month"].unique())},
    labels={
        "month": "Month",
        "white_win_rate_percent": "White Win Rate (%)"
    }
)

# Style
fig.update_layout(
    height=1000,
    plot_bgcolor="white",
    showlegend=False,
    yaxis=dict(range=[0, 100]),
    margin=dict(t=60, l=20, r=20, b=40)
)

fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))  # Clean titles
fig.update_yaxes(matches=None)  # Let each subplot have its own scale if needed
fig.update_xaxes(tickangle=45)

fig.show()
