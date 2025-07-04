import os
import json
from scripts.get_wnba_game_ids import get_game_ids  # or wherever you moved it

def main():
    output_path = "data/wnba_2025_game_ids.json"

    # Load existing file (if it exists)
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            existing_ids = set(json.load(f))
    else:
        existing_ids = set()

    # Get new game IDs (update date range as needed)
    new_ids = get_game_ids("20250704", "20250711", exclude_dates=["20250701"])

    # Merge
    combined_ids = sorted(existing_ids.union(new_ids))

    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save
    with open(output_path, "w") as f:
        json.dump(combined_ids, f, indent=2)

    print(f"✅ Added {len(new_ids)} new IDs → Total: {len(combined_ids)}")


if __name__ == "__main__":
    main()