from bs4 import BeautifulSoup
import requests

import asyncio
from crawl4ai import *
import re



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

    async def extract_urls(self, url: str) -> list:
        '''
        extract_urls

        Description:
        This method extracts URLs from a given url.

        Params: 
        url: str - The URL of the page to scrape.

        Returns:
        list - A list of articles extracted from the page.
        '''

        # 1) A BM25 filter with a user query
        bm25_filter = BM25ContentFilter(
            user_query="news press reports market stock",
            # Adjust for stricter or looser results
            bm25_threshold=1.0  
        )

        # Step 2: Create a content filter
        md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)

        # Step 3: Create a crawler
        config = CrawlerRunConfig(
            markdown_generator=md_generator,
            exclude_external_links=True,
            excluded_tags=['script', 'style', 'noscript', 'img'],  # Exclude unwanted tags
        )

        final_list = []

        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url=url,
                config=config
            )

            
            if result.success:
                # 'fit_markdown' is your pruned content, focusing on "denser" text
                print("Raw Markdown length:", len(result.markdown.raw_markdown))
                print("Fit Markdown length:", len(result.markdown.fit_markdown))

                markdown_result = result.markdown.fit_markdown

                print("fitted markdown: ", markdown_result)
                extract_regex = r'(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+'
                http_urls = re.findall(extract_regex, markdown_result)
                print("Extracted URLs:", http_urls)
                final_list.append(http_urls)
            else:
                print("Error:", result.error_message)
        

        return final_list

    async def get_article_info(self, url: str) -> str:
        '''
        get_article_info

        Description:
        This method fetches the article content from the specified URL.

        Params: 
        url: str - The URL of the page to scrape.

        Returns:
        str - The article content of the page.
        '''

        print("get_article_info \n")
        # bm25_filter = BM25ContentFilter(
        #     user_query="price stock market",
        #     # Adjust for stricter or looser results
        #     bm25_threshold=1.0  
        # )

        # # Step 2: Create a content filter
        # md_generator = DefaultMarkdownGenerator(content_filter=bm25_filter)

        prune_filter = PruningContentFilter(
            threshold=0.5,  # Adjust this threshold to control the pruning level
            threshold_type='dynamic',  # Tags to prune
            min_word_threshold=10,  # Minimum number of words to keep
        )

        # Step 2: Create a content filter
        md_generator = DefaultMarkdownGenerator(content_filter=prune_filter)

        # Step 3: Create a crawler
        config = CrawlerRunConfig(
            # markdown_generator=md_generator,
            exclude_external_links=True,
            excluded_tags=['script', 'style', 'noscript', 'header', 'footer'],  # Exclude unwanted tags

        )

        final_result = ''

        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(
                url=url,
                config=config
            )

            
            if result.success:
                # 'fit_markdown' is your pruned content, focusing on "denser" text
                print("Raw Markdown length:", len(result.markdown.raw_markdown))
                print("Fit Markdown length:", len(result.markdown.fit_markdown))

                markdown_result = result.markdown.raw_markdown

                print("fitted markdown: ", markdown_result)

                final_result = str(markdown_result)
            else:
                print("Error:", result.error_message)
        

        return final_result

if __name__ == "__main__":
    scraper = ScrapingWebsite('https://www.cnbc.com/pro/news/')
    #scraper.extract_urls_articles(scraper.url)
    #asyncio.run(scraper.extract_urls("https://www.bloomberg.com/"))
    asyncio.run(scraper.get_article_info("https://www.cnbc.com/2025/06/24/jpmorgan-traders-say-its-time-to-get-bulled-up-again.html"))

# scraper = ScrapingWebsite('https://stellar.org/')
# soup = scraper.parse_html()
# #print(soup.prettify())
# print(soup.text)

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())