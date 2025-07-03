
import sys
import os                                                           
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
 
import scripts.step1_call_api as sca
from utils.browser import open_browser_and_submit_form  #Imports the URL generator and browser automation.

def run_all():
    candidates = sca.get_urls_for_all("data/input.csv")#Starts the process and gets all enriched candidates.

    for candidate in candidates:
        print(f"[INFO] Submitting for {candidate['name']}")          
        open_browser_and_submit_form(candidate["submission_url"], candidate) #Loops through and submits forms.

if __name__ == "__main__":
    run_all()
