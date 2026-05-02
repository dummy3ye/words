import re
import os

DUMP_FILE = "internal/dump.txt"
SEMI_FILE = "internal/semi.txt"

def clean_data():
    try:
        if not os.path.exists(DUMP_FILE):
            print(f"[!] {DUMP_FILE} not found.")
            return

        with open(DUMP_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        cleaned = re.sub(r'[^a-zA-Z]', ' ', content)
        words = cleaned.lower().split()
        
        os.makedirs("internal", exist_ok=True)
        with open(SEMI_FILE, "w", encoding="utf-8") as f:
            f.write(" ".join(words))
            
        print(f"[+] Data cleaned. Saved to {SEMI_FILE}.")
        
    except Exception as e:
        print(f"[!] Cleaning failed: {e}")

if __name__ == "__main__":
    clean_data()
