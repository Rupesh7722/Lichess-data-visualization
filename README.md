# 🧠 Chess Openings Visual Analysis using Lichess Data

This project explores and visualizes chess opening trends using 7 months of real-world data from [Lichess.org](https://lichess.org/). By analyzing millions of games, it reveals insights into opening popularity, effectiveness, and player behavior — empowering data-driven decision-making in chess.

---

## 📌 Problem Statement

With thousands of games played daily online, chess players often struggle to identify which openings are most effective across ratings and time. This project solves that by visualizing opening performance trends over time.

---

## 🎯 Objectives

- Extract and clean 7 months of game data from Lichess (PNG format)
- Merge into a single structured dataset
- Visualize trends in opening usage, win/loss/draw outcomes, and rating distributions
- Derive actionable insights for players and strategists

---

## 📁 Data Collection & Preprocessing

- **Source:** Monthly game archives from [Lichess.org](https://database.lichess.org/)
- **Format:** PNG (Portable Game Notation) parsed using custom Python scripts
- **Cleaning:** Removed invalid records, filtered by time control, merged by date

### 📊 Dataset Columns

- Game date
- Player ELOs (white/black)
- Opening name & ECO code
- Game outcome (win/loss/draw)
- Opening length, time control

---

## 🛠️ Tools & Technologies

| Category | Tools |
|----------|-------|
| Language | Python |
| Libraries | `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` |
| IDE | Visual Studio Code |
| Source | [lichess.org](https://lichess.org/), 7-month dataset |

---

## 📈 Key Visualizations

- 📍 **Sunburst Chart:** Popularity and win ratio of openings  
- 📍 **Animated Line Chart:** Time-based usage trends of specific openings  
- 📍 **Facet Line Chart:** Volatility of openings like Scandinavian and London  
- 📍 **Box Plot & KDE:** Opening usage by rating cluster   

---

## 🧠 Insights & Observations

- **Queen’s Pawn** is the most consistently played and has high draw ratios  
- **Caro-Kann** is favored among defensive players  
- **Van’t Kruij’s Opening** shows erratic usage patterns  
- Most popular openings are used by players with ~1800 ELO  
- High-risk openings correlate with volatile win/loss rates  

---

## 🔁 Project Workflow

1. **Data Extraction:** PNG parsing and PGN file read
2. **Preprocessing:** Merge, clean, filter, deduplicate
3. **Visualization:** Generate charts using Python libraries
4. **Insight Generation:** Trend analysis, outcome mapping

---

## 🚀 Future Scope

- Build interactive dashboards using **Plotly Dash**
- Track **real-time game stats** and **geo-based trends**
- Train **deep learning models** for opening move predictions

---

## ✅ Conclusion

This project merges chess strategy with data science, proving that visual analytics can help players refine their game. It promotes **data-driven thinking** in competitive strategy — on and off the board.

---

## 👤 Author

**Rupesh Sharma**  
B.Tech CSE (Data Science), Punjab Engineering College  
[LinkedIn](https://www.linkedin.com/in/rupesh-sharma-334887315/) • [GitHub](https://github.com/Rupesh7722)
