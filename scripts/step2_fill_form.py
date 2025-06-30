from utils.browser import open_browser_and_submit_form
from scripts.step1_call_api import get_urls_for_all


def submit_forms(candidates):
    """
    For each candidate, open the URL and submit the form.
    """
    for candidate in candidates:
        url = candidate.get("submission_url")
        if not url:
            print(f"[SKIPPED] No URL for {candidate['name']}")
            continue

        print(f"[INFO] Submitting form for {candidate['name']}")
        open_browser_and_submit_form(url, candidate)


if __name__ == "__main__":
    candidates = get_urls_for_all("data/input.csv")
    submit_forms(candidates)
