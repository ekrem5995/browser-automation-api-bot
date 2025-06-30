#This script:

#Loads a list of candidates from a CSV file.

#Calls an API function (get_submission_url) for each one to get their form submission URL.

#Adds that URL into each candidate's data.

#Prints out names with their unique submission links.

import pandas as pd
from utils.api import get_submission_url


def load_candidates(csv_path):
    """
    Load candidate data from a CSV file.
    """
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")


def get_urls_for_all(csv_path):
    """
    Loop through all candidates and get their submission URLs.
    """
    candidates = load_candidates(csv_path)
    for candidate in candidates:
        candidate["submission_url"] = get_submission_url(candidate)
    return candidates


if __name__ == "__main__":
    # Test run
    candidates = get_urls_for_all("data/input.csv")
    for c in candidates:
        print(f"{c['name']} → {c['submission_url']}")

