#file structure

# [Event "Rated Blitz game"]
# [Site "https://lichess.org/abc123"]
# [Date "2025.03.15"]
# [White "SuperPlayer"]
# [Black "MegaOpponent"]
# [WhiteElo "1850"]
# [BlackElo "1800"]
# [Result "1-0"]
# [TimeControl "300+0"]
# [ECO "C50"]
# [Opening "Italian Game"]

# 1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d4 ...









import chess.pgn
import pandas as pd
from tqdm import tqdm
import os
import zstandard as zstd
import io

# === Configuration ===
PGN_ZST_FILE = "lichess_db_standard_rated_2024-09.pgn.zst"  # Path to your PGN file
OUTPUT_CSV = "lichess_augmented_100k_sep.csv"  # Path to save the cleaned data
LIMIT = 100000  # Limit for testing, change to None for all games

# Function to normalize result values (White, Black, Draw)
def normalize_result(result):
    if result == "1-0":
        return "White"
    elif result == "0-1":
        return "Black"
    elif result == "1/2-1/2":
        return "Draw"
    return None

# Function to parse and clean the PGN file
def parse_pgn_zst_file(zst_file_path, limit=LIMIT):
    games_data = []

    with open(zst_file_path, "rb") as fh:
        dctx = zstd.ZstdDecompressor()
        with dctx.stream_reader(fh) as reader:
            text_stream = io.TextIOWrapper(reader, encoding='utf-8')
            
            for _ in tqdm(range(limit)):
                game = chess.pgn.read_game(text_stream)
                if game is None:
                    break
                
                headers = game.headers
                
                # Extract ratings, result, winner color
                white_elo = int(headers.get("WhiteElo", 0))
                black_elo = int(headers.get("BlackElo", 0))
                avg_elo = (white_elo + black_elo) // 2
                rating_diff = abs(white_elo - black_elo)
                result = headers.get("Result", "*")
                winner = normalize_result(result)

                # Extract game length (number of moves)
                moves = list(game.mainline_moves())
                game_length = len(moves)
                
                

                # Collect data for each game
                games_data.append({
                    "date": headers.get("UTCDate", headers.get("Date", None)),
                    "white": headers.get("White"),
                    "black": headers.get("Black"),
                    "white_rating": white_elo,
                    "black_rating": black_elo,
                    "avg_elo": avg_elo,
                    "rating_diff": rating_diff,
                    "result": result,
                    "winner_color": winner,
                    "opening_eco": headers.get("ECO"),
                    "opening_name": headers.get("Opening"),
                    "time_control": headers.get("TimeControl"),
                    "game_length": game_length,  # This line adds the game_length column
                })

    # Convert to DataFrame
    df = pd.DataFrame(games_data)

    # Save to CSV
    df.to_csv(OUTPUT_CSV, index=False)
    print(f"\n✅ Saved cleaned data to {OUTPUT_CSV}")

    return df


# Main function
if __name__ == "__main__":
    print("🔍 Parsing and cleaning PGN data...")

    # Parse the data and clean it
    df = parse_pgn_zst_file(PGN_ZST_FILE)

    print("\n📊 Sample cleaned DataFrame:")
    print(df.head())
