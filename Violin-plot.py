import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Categorize time control (simple)
def categorize(tc):
    base = int(tc.split('+')[0]) if '+' in tc else 0
    if base < 180: return "Bullet"
    elif base < 600: return "Blitz"
    elif base < 1800: return "Rapid"
    else: return "Classical"

df["time_category"] = df["time_control"].apply(categorize)

# Simple violin plot
fig = px.violin(
    df,
    x="time_category",
    y="game_length",
    box=True,
    points="all",
    title="Game Lengths by Time Category"
)
fig.show()
