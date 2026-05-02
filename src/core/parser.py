import json
import os
from collections import defaultdict
from src.utils.logger import get_logger

logger = get_logger("Parser")

class WordsParser:
    def __init__(self, rules_path, input_path, output_dir):
        self.rules = json.load(open(rules_path))
        self.input_path = input_path
        self.output_dir = output_dir

    def parse(self):
        with open(self.input_path, "r", encoding="utf-8") as f:
            words = f.read().split()
            
        groups = defaultdict(list)
        for w in words:
            if w: groups[w[0]].append(w)
            
        output = []
        log = []
        for letter in sorted(groups.keys()):
            if output: output.append("")
            l_words = sorted(groups[letter]) if self.rules.get("sort_alphabetical") else groups[letter]
            
            chunk_size = self.rules.get("max_words_per_line", 100)
            for i in range(0, len(l_words), chunk_size):
                chunk = l_words[i:i+chunk_size]
                output.append(" ".join(chunk))
                log.append({"letter": letter, "count": len(chunk)})
                
        os.makedirs(self.output_dir, exist_ok=True)
        with open(os.path.join(self.output_dir, "words.txt"), "w") as f:
            f.write("\n".join(output))
        logger.info("Parsing complete.")
