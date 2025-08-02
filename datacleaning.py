import chess.pgn
import pandas as pd

PGN_FILE = "lichess_games.pgn"   # normal PGN file
OUTPUT_CSV = "lichess_cleaned.csv"
LIMIT = 100000                   # read only first 1000 games for example

def normalize_result(result):
    if result == "1-0": return "White"
    if result == "0-1": return "Black"
    if result == "1/2-1/2": return "Draw"
    return None

games_data = []

with open(PGN_FILE) as pgn:
    for i in range(LIMIT):
        game = chess.pgn.read_game(pgn)
        if game is None:
            break

        headers = game.headers
        moves = list(game.mainline_moves())

        games_data.append({
            "date": headers.get("Date"),
            "white": headers.get("White"),
            "black": headers.get("Black"),
            "white_rating": headers.get("WhiteElo"),
            "black_rating": headers.get("BlackElo"),
            "result": headers.get("Result"),
            "winner_color": normalize_result(headers.get("Result")),
            "opening_name": headers.get("Opening"),
            "time_control": headers.get("TimeControl"),
            "game_length": len(moves)
        })

# Save to CSV
df = pd.DataFrame(games_data)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved {len(df)} games to {OUTPUT_CSV}")
print(df.head())
