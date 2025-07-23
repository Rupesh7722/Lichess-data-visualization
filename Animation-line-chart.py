import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.cm as cm

# Load the dataset
df = pd.read_csv("lichess_merged_7months.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)

# Filter out missing opening names
df = df.dropna(subset=["opening_name"])

# 🔝 Top 10 most frequent openings
top_openings = df["opening_name"].value_counts().nlargest(10).index.tolist()
df_top = df[df["opening_name"].isin(top_openings)]

# 📊 Pivot table: rows = months, columns = openings, values = count
month_order = sorted(df["month"].unique())
pivot = df_top.groupby(["month", "opening_name"]).size().unstack(fill_value=0).reindex(month_order)

# Setup plot
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(14, 7))

# 🎨 Use tab10 colormap for 10 distinct colors
colors = cm.get_cmap('tab10', 10)

lines = {}
for idx, opening in enumerate(top_openings):
    line, = ax.plot([], [], label=opening, linewidth=2.5, color=colors(idx))
    lines[opening] = line

ax.set_xlim(-0.5, len(month_order) - 0.5)
ax.set_ylim(0, pivot.values.max() + 50)
ax.set_xticks(range(len(month_order)))
ax.set_xticklabels(month_order, rotation=30, ha="right")
ax.set_xlabel("Month", fontsize=13)
ax.set_ylabel("Number of Games", fontsize=13)
ax.set_title("📈 Top 10 Chess Openings Popularity Over Time", fontsize=18, weight="bold")
ax.legend(title="Openings", loc="upper left", bbox_to_anchor=(1.02, 1.0))
ax.grid(True)

# 🌀 Animation update function
def update(frame):
    for opening in top_openings:
        y_vals = pivot[opening].values[:frame + 1]
        x_vals = list(range(frame + 1))
        lines[opening].set_data(x_vals, y_vals)
    return lines.values()

# 🎞 Animate
ani = FuncAnimation(fig, update, frames=len(month_order), interval=1000, repeat=False)

plt.tight_layout()
plt.show()
