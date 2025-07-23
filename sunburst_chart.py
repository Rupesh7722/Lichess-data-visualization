import pandas as pd
import plotly.express as px

# Load cleaned dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Drop rows with missing values
df_clean = df.dropna(subset=["opening_name", "result", "winner_color"])

# 🔥 Define list of famous/popular openings to focus on
popular_openings = [
    "Queen's Pawn Game",
    "Caro-Kann Defense",
    "Van't Kruijs Opening",
    "Modern Defense",
    "Queen's Pawn Game: Accelerated London System",
    "Philidor Defense",
    "Pirc Defense",
    "Horwitz Defense",
    "Scandinavian Defense",
    "French Defense: Knight Variation",
    "Scandinavian Defense: Mieses-Kotroc Variation",
    "Owen Defense",
    "Indian Defense",
    "Queen's Pawn Game: Modern Defense",
    "Hungarian Opening"
]


# Filter only these openings
df_filtered = df_clean[df_clean["opening_name"].isin(popular_openings)]

# Group data
sunburst_data = df_filtered.groupby(
    ["opening_name", "result", "winner_color"]
).size().reset_index(name='count')

# Sunburst chart
fig = px.sunburst(
    sunburst_data,
    path=["opening_name", "result", "winner_color"],
    values='count',
    color='winner_color',
    color_discrete_map={
        "White": "#1f77b4",
        "Black": "#d62728",
        "Draw": "#2ca02c"
    },
    title="Opening Outcome Sunburst Chart (Popular Openings)"
)

fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.show()
