import requests
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup

JSON_FILE = "urls.json"
DUMP_FILE = "internal/dump.txt"

def harvest_data():
    if not os.path.exists(JSON_FILE):
        print(f"[!] {JSON_FILE} not found. Run 'node src/urls.js' first.")
        return

    os.makedirs("internal", exist_ok=True)

    with open(JSON_FILE, "r") as f:
        urls_data = json.load(f)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    updated = False

    for entry in urls_data:
        if not entry["scraped"]:
            url = entry["url"]
            print(f"[*] Fetching raw data from {url}...")
            
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.text, "html.parser")
                raw_text = soup.get_text(separator=" ")
                
                with open(DUMP_FILE, "a", encoding="utf-8") as f:
                    f.write("\n" + raw_text)
                
                entry["scraped"] = True
                entry["last_scraped"] = datetime.now().isoformat()
                entry["tokens_count"] = len(raw_text.split())
                updated = True
                print(f"[+] Scraped {url}. Tokens: {entry['tokens_count']}")
                
            except Exception as e:
                print(f"[!] Scrape failed for {url}: {e}")

    if updated:
        with open(JSON_FILE, "w") as f:
            json.dump(urls_data, f, indent=2)
        print("[+] urls.json updated.")
    else:
        print("[~] No new URLs to scrape.")

if __name__ == "__main__":
    harvest_data()
