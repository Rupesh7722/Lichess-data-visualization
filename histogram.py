import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("lichess_merged_7months.csv")  # Replace with your actual file name

# Ensure avg_elo is numeric
df['avg_elo'] = pd.to_numeric(df['avg_elo'], errors='coerce')

# Filter for top 10 most popular openings
top_openings = df['opening_name'].value_counts().head(10).index
filtered_df = df[df['opening_name'].isin(top_openings)]

# Plot KDE for average ELO
plt.figure(figsize=(10, 6))
sns.kdeplot(filtered_df['avg_elo'].dropna(), shade=True, color="mediumseagreen", linewidth=2)
plt.title('KDE Curve for Average ELO (Top 10 Openings)', fontsize=16)
plt.xlabel('Average ELO')
plt.ylabel('Density')
plt.grid(True)
plt.show()
