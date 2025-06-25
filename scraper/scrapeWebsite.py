from bs4 import BeautifulSoup
import requests

import asyncio
from crawl4ai import *

async def main():
    # Step 1: Create a pruning filter
    # prune_filter = PruningContentFilter(
    #     # Lower → more content retained, higher → more content pruned
    #     threshold=0.45,           
    #     # "fixed" or "dynamic"
    #     threshold_type="dynamic",  
    #     # Ignore nodes with <5 words
    #     min_word_threshold=5      
    # )

    # 1) A BM25 filter with a user query
    bm25_filter = BM25ContentFilter(
        user_query="news, press, or reports",
        # Adjust for stricter or looser results
        bm25_threshold=1.2  
    )

    # Step 2: Create a content filter
    md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)

    # Step 3: Create a crawler
    config = CrawlerRunConfig(
        markdown_generator=md_generator
    )

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://stellar.org/",
            config=config
        )
        print(result.markdown.fit_markdown)
        if result.success:
            # 'fit_markdown' is your pruned content, focusing on "denser" text
            print("Raw Markdown length:", len(result.markdown.raw_markdown))
            print("Fit Markdown length:", len(result.markdown.fit_markdown))
        else:
            print("Error:", result.error_message)

if __name__ == "__main__":
    asyncio.run(main())

class ScrapingWebsite:
    def __init__(self, url:str):
        '''
        ___init__

        Description:
        This is the contructor for the scrapingWebsite class. Here we initialize the URL that we want to scrape.

        Params:
        url: str - The URL of the website to scrape.
        '''
        self.newsOutlets = ['https://www.cnbc.com/', 'https://www.bloomberg.com/', 'https://finance.yahoo.com/news/', 'https://www.nbcnews.com/business', 'https://www.reuters.com/finance/markets/', 'https://www.marketwatch.com/', 'https://www.wsj.com/']
        self.url = url
        self.html = self.get_html()
        self.soup = self.parse_html()

    def extract_articles(self):
        '''
        extract_articles

        Description:
        This method extracts articles from the HTML content of the page.

        Params: 
        None

        Returns:
        list - A list of articles extracted from the page.
        '''
        # articles = []
        # for article in self.soup.find_all('article'):
        #     articles.append(article.text)
        # return articles
        pass

    def get_article(self) -> str:
        '''
        get_article

        Description:
        This method fetches the article content from the specified URL.

        Params: 
        None

        Returns:
        str - The article content of the page.
        '''
        # if self.url == '' or self.url is None:
        #     raise ValueError('You must have valid url to parse.')

        # response = requests.get(self.url)
        # return response.text
        pass


# scraper = ScrapingWebsite('https://stellar.org/')
# soup = scraper.parse_html()
# #print(soup.prettify())
# print(soup.text)

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())