# 🧠 Browser Automation API Bot

A modular Python automation bot that:
- Loads candidate data from CSV
- Calls an API to generate unique submission URLs
- Auto-fills and submits web forms using Selenium
- Logs success/failure to a report

---

## 🚀 Use Case

Ideal for:
- Automating form submissions (job applications, surveys, onboarding)
- Testing browser-based workflows
- Mass personal form submissions using CSV data

---

## 📁 Project Structure

```
browser_automation_api_bot/
├── scripts/
│   ├── step1_call_api.py         # Load CSV and call API
│   ├── step2_browser_submit.py   # Loop and submit using browser
│   └── step3_report_done.py      # Logs each submission
│
├── utils/
│   ├── api.py                    # Fake API handler (placeholder)
│   └── browser.py                # Selenium automation logic
│
├── data/
│   ├── input.csv                 # Candidate list
│   └── submission_report.csv     # Log file
│
├── .env                          # Environment variables
├── main.py                       # Runs the full workflow
├── run.py                        # Entry point
├── requirements.txt              # Dependencies
└── README.md                     # Project docs
```

---

## ⚙️ How It Works

### Step 1 – Call API and Generate Links
```python
# scripts/step1_call_api.py
import pandas as pd
from utils.api import get_submission_url

def load_candidates(csv_path):
    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")

def get_urls_for_all(csv_path):
    candidates = load_candidates(csv_path)
    for candidate in candidates:
        candidate["submission_url"] = get_submission_url(candidate)
    return candidates
```

### Step 2 – Auto Submit Forms
```python
# utils/browser.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from scripts.step3_report_done import log_submission
from time import sleep

def open_browser_and_submit_form(url, candidate):
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        # Fill form here using driver.find_element(By.ID, "...")
        # Example:
        # driver.find_element(By.NAME, "name").send_keys(candidate["name"])
        # driver.find_element(By.NAME, "email").send_keys(candidate["email"])
        # driver.find_element(By.TAG_NAME, "button").click()
        log_submission(candidate, success=True)
    except Exception as e:
        print(f"[ERROR] Failed for {candidate['name']}: {e}")
        log_submission(candidate, success=False)
    finally:
        driver.quit()
```

### Step 3 – Log Results
```python
# scripts/step3_report_done.py
import csv
from datetime import datetime

def log_submission(candidate, success=True):
    with open("data/submission_report.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(timespec="seconds"),
            candidate["name"],
            candidate["email"],
            candidate.get("submission_url", ""),
            "SUCCESS" if success else "FAILED"
        ])
```

---

## 🧪 How To Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run the Bot
```bash
python run.py
```

It will read `data/input.csv`, submit the form for each candidate, and log results.

---

## 🛠 Technologies
- Python
- Selenium
- Pandas
- dotenv

---

## ✅ What I Learned
- Modularizing Python code with folders like `scripts` and `utils`
- Using Selenium for browser automation
- Writing clear CSV and form automation workflows
- Logging success/failure automatically

---

## 📌 Example Use Cases
- Submitting scholarship or internship forms automatically
- Filling the same contact form for multiple users
- QA testing front-end forms

---

## 🌍 GitHub Setup
```bash
git init
git add .
git commit -m "Initial commit - browser automation bot"
git remote add origin https://github.com/ekrem5995/browser-automation-api-bot
git branch -M main
git push -u origin main
```

---

Now you're ready to use or share this project on GitHub, Upwork, or LinkedIn!
