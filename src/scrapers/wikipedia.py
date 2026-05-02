import requests
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
from src.utils.logger import get_logger

logger = get_logger("Scraper")
JSON_FILE = "urls.json"
DUMP_FILE = "internal/dump.txt"

class Scraper:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0"}

    def run(self):
        if not os.path.exists(JSON_FILE):
            logger.error("urls.json not found")
            return

        with open(JSON_FILE, "r") as f:
            urls_data = json.load(f)

        for entry in urls_data:
            if not entry["scraped"]:
                try:
                    res = requests.get(entry["url"], headers=self.headers)
                    res.raise_for_status()
                    soup = BeautifulSoup(res.text, "html.parser")
                    text = soup.get_text(separator=" ")
                    
                    with open(DUMP_FILE, "a", encoding="utf-8") as f:
                        f.write("\n" + text)
                    
                    entry.update({
                        "scraped": True,
                        "last_scraped": datetime.now().isoformat(),
                        "tokens_count": len(text.split())
                    })
                    logger.info(f"Scraped {entry['url']}")
                except Exception as e:
                    logger.error(f"Failed {entry['url']}: {e}")

        with open(JSON_FILE, "w") as f:
            json.dump(urls_data, f, indent=2)
