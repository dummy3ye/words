import os

SEMI_FILE = "internal/semi.txt"
BLACKLIST_FILE = "config/blacklist.txt"
MIN_LENGTH = 3

def remove_duplicates():
    try:
        if not os.path.exists(SEMI_FILE):
            print(f"[!] {SEMI_FILE} not found.")
            return

        # Load blacklist if it exists
        blacklist = set()
        if os.path.exists(BLACKLIST_FILE):
            with open(BLACKLIST_FILE, "r", encoding="utf-8") as f:
                blacklist = set(line.strip().lower() for line in f if line.strip())

        with open(SEMI_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        
        words = content.split()
        
        # Apply filters: unique, length, and blacklist
        unique_filtered = []
        seen = set()
        
        for word in words:
            word = word.lower()
            if word not in seen and len(word) >= MIN_LENGTH and word not in blacklist:
                unique_filtered.append(word)
                seen.add(word)
        
        unique_filtered.sort()
        
        with open(SEMI_FILE, "w", encoding="utf-8") as f:
            f.write(" ".join(unique_filtered))
            
        print(f"[+] Cleanup complete:")
        print(f"    - Filtered out {len(words) - len(unique_filtered)} words (junk/duplicates).")
        print(f"    - Final unique words: {len(unique_filtered)}")
        
    except Exception as e:
        print(f"[!] Cleanup failed: {e}")

if __name__ == "__main__":
    remove_duplicates()
