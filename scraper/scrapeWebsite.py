from bs4 import BeautifulSoup
import requests

class ScrapingWebsite:
    def __init__(self, url:str):
        '''
        ___init__

        Description:
        This is the contructor for the scrapingWebsite class. Here we initialize the URL that we want to scrape.

        Params:
        url: str - The URL of the website to scrape.
        '''
        self.url = url
        self.html = self.get_html()
        self.soup = self.parse_html()

    def get_html(self) -> str:
        '''
        get_html

        Description:
        This method fetches the HTML content of the specified URL.

        Params: 
        None

        Returns:
        str - The HTML content of the page.
        '''

        if self.url == '' or self.url is None:
            raise ValueError('You must have valid url to parse.')

        response = requests.get(self.url)
        return response.text

    def parse_html(self):
        # must come back to create comments about this method

        if self.html == '' or self.html is None:
            raise ValueError('You must have valid html to parse.')
        soup = BeautifulSoup(self.html, 'html.parser')
        return soup


scraper = ScrapingWebsite('https://stellar.org/')
soup = scraper.parse_html()
#print(soup.prettify())
print(soup.text)

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())