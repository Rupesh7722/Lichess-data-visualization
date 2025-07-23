import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv("lichess_merged_7months.csv")

# Map time control to category
def categorize_time_control(tc):
    try:
        base = int(tc.split('+')[0])  # Get base time in seconds
    except:
        return "Unknown"
    if base < 180:
        return "Bullet"
    elif base < 600:
        return "Blitz"
    elif base < 1800:
        return "Rapid"
    else:
        return "Classical"

# Create new column with human-readable labels
df['time_control_category'] = df['time_control'].apply(categorize_time_control)

# Use only top 7 raw time controls to keep plot clean
top_time_controls = df['time_control'].value_counts().nlargest(7).index
df = df[df['time_control'].isin(top_time_controls)]

# Create violin plot with readable labels
fig = px.violin(
    df,
    x="time_control_category",
    y="game_length",
    box=True,
    points="all",
    color="time_control_category",
    title="Distribution of Game Lengths by Time Control Category",
    labels={
        "time_control_category": "Time Control",
        "game_length": "Game Length (Moves)"
    }
)

fig.update_layout(showlegend=False, template="plotly_white")
fig.show()



# time Control Category Mapping (based on Lichess):

# Time (Seconds)	Category
# < 180	Bullet
# 180 - 599	Blitz
# 600 - 1799	Rapid
# ≥ 1800	Classical