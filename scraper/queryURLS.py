from googlesearch import search

class QueryData():
    '''
    QueryData

    Description
    This is a class to perform a search query and return the desired results.
    '''

    def __init__(self, query:str):
        '''
        __init__

        Description
        This is the constructor for the GoogleQuery class.
        It initializes the class with no parameters.
        '''
        self.query = query
        self.urls = []

    def changeQuery(self, query:str):
        '''
        changeQuery

        Description
        This is a method to change the query of the GoogleQuery class.
        It takes a string as a parameter and sets the query attribute to that string.

        Params
        query: str - The new query string to set for the QueryData class.
        '''
        self.query = query
    
    def queryGoogle(self, numPerRequest:int = 10, totalRequest:int = 10, pause:float = 2) -> list[str]:
        '''
        queryGoogleUrls

        Description
        This is a method to perform a Google search query and return the URLS of the results.
        To be honest I've never used this package before I was struggling to find a way to get results 
        from Google without using the API, so I found this package and it seems to work well.

        The documentation is not existant but I give credit were credit is due: https://pypi.org/project/google/3.0.0/#description
        The website I used to learn about the package is geeks for geeks: https://www.geeksforgeeks.org/python/performing-google-search-using-python-code/

        Params
        numPerRequest: int - The number of results each request sends back (default is 10)
        totalRequest: int - The total number of results that google returns (default is 10)
        pause: int - The number of seconds to wait between requests (default is 2)

        Returns
        list[str] - A list of URLs returned by the Google search query.

        '''

        # set up an algorithm to help with rate limiting
        if(numPerRequest > totalRequest):
            print("Trust me bro I'm saving you from getting rate limited :)")
            raise ValueError("The number of results requested cannot be greater than the total number of results returned by Google.")
    
        for j in search(self.query, tld="co.in", num=numPerRequest, stop=totalRequest, pause=pause):
            self.urls.append(j)
        
        return self.urls

    
# queryingTest = QueryData("stellar lumens cryptocurrency news")
# print(queryingTest.queryGoogle(numPerRequest=10, totalRequest=10, pause=5))