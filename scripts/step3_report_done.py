import csv
import os
from datetime import datetime

def log_submission(candidate, success=True):
    filepath = "data/submission_report.csv"
    file_exists = os.path.isfile(filepath)

    with open(filepath, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        # Write header only once
        if not file_exists:
            writer.writerow(["timestamp", "name", "email", "submission_url", "status"])

        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            candidate.get("name", ""),
            candidate.get("email", ""),
            candidate.get("submission_url", ""),
            "SUCCESS" if success else "FAILED"
        ])
