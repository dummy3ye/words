from src.scrapers.wikipedia import Scraper as WikipediaScraper
from src.core.parser import WordsParser
from src.utils.logger import get_logger

logger = get_logger("Orchestrator")

def run():
    logger.info("Starting pipeline")
    
    # Scrape
    scraper = WikipediaScraper()
    scraper.run()
    
    # Parse
    parser = WordsParser("config/rulesets.json", "internal/semi.txt", "dist")
    parser.parse()
    
    logger.info("Pipeline complete")

if __name__ == "__main__":
    run()
