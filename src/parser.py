import json
import os
from collections import defaultdict

RULES_FILE = "config/rulesets.json"
SEMI_FILE = "internal/semi.txt"
OUTPUT_DIR = "dist"

def parse_words():
    try:
        with open(RULES_FILE, "r") as f:
            rules = json.load(f)
        
        with open(SEMI_FILE, "r", encoding="utf-8") as f:
            words = f.read().split()
            
        groups = defaultdict(list)
        for word in words:
            if word:
                groups[word[0]].append(word)
        
        output_lines = []
        linear_log = []
        
        for letter in sorted(groups.keys()):
            if output_lines:
                output_lines.append("")
                
            letter_words = groups[letter]
            if rules.get("sort_alphabetical"):
                letter_words.sort()
            
            max_words = rules.get("max_words_per_line", 100)
            
            for i in range(0, len(letter_words), max_words):
                chunk = letter_words[i : i + max_words]
                output_lines.append(" ".join(chunk))
                linear_log.append({
                    "letter": letter,
                    "count": len(chunk),
                    "range": f"{i}-{i+len(chunk)}"
                })
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(os.path.join(OUTPUT_DIR, "words.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))
            
        with open(os.path.join(OUTPUT_DIR, "linear.json"), "w", encoding="utf-8") as f:
            json.dump(linear_log, f, indent=2)
            
        print(f"[+] Parsing complete. Results in {OUTPUT_DIR}/ folder.")
        
    except Exception as e:
        print(f"[!] Parsing failed: {e}")

if __name__ == "__main__":
    parse_words()
