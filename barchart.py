import pandas as pd
import plotly.graph_objects as go

# Load the data
df = pd.read_csv("lichess_merged_7months.csv")

# Drop rows with missing data
df = df.dropna(subset=["opening_name", "white", "black"])

# Count total games per opening
opening_counts = df["opening_name"].value_counts().rename_axis("opening").reset_index(name="total_games")

# Get top 15 most common openings
top_openings = opening_counts.head(15)

# === Plot horizontal bar chart ===
fig = go.Figure(go.Bar(
    x=top_openings["total_games"],
    y=top_openings["opening"],
    orientation='h',
    marker_color='mediumpurple'
))

# Layout formatting
fig.update_layout(
    title="♟️ Most Common Chess Openings (Overall)",
    xaxis_title="Number of Games",
    yaxis_title="Opening Name",
    font=dict(size=14),
    height=600,
    width=900,
    plot_bgcolor="white",
)

# Reverse y-axis to show highest bars on top
fig.update_yaxes(autorange="reversed")

fig.show()
