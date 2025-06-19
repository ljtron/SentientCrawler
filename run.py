from scraper import queryURLS 

queryingTest = queryURLS.QueryData("stellar lumens cryptocurrency news")
print(queryingTest.queryGoogle(numPerRequest=10, totalRequest=10, pause=5))