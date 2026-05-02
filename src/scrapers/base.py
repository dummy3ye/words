from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def scrape(self, url):
        pass

class WikipediaScraper(BaseScraper):
    def scrape(self, url):
        # Move your BeautifulSoup logic here
        return "Scraped content"
