import scripts.step3_report_done as srd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def open_browser_and_submit_form(url, candidate):
    """
    Opens browser, navigates to URL, fills and submits form.
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        sleep(2)

        # Fill form fields (adjust these selectors for your actual form)
        name_input = driver.find_element(By.NAME, "name")
        email_input = driver.find_element(By.NAME, "email")
        message_input = driver.find_element(By.NAME, "message")

        name_input.send_keys(candidate["name"])
        email_input.send_keys(candidate["email"])
        message_input.send_keys("This is an automated test message.")

        # Submit button
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        sleep(2)  # Let the form submit
        srd.log_submission(candidate, success=True)

    except Exception as e:
        print(f"[ERROR] Failed to submit form for {candidate['name']}: {e}")
        srd.log_submission(candidate, success=False)

    finally:
        driver.quit()
