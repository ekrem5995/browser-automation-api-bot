
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import scripts.step1_call_api as sca
from utils.browser import open_browser_and_submit_form

def run_all():
    candidates = sca.get_urls_for_all("data/input.csv")

    for candidate in candidates:
        print(f"[INFO] Submitting for {candidate['name']}")
        open_browser_and_submit_form(candidate["submission_url"], candidate)

if __name__ == "__main__":
    run_all()
