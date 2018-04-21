
def poll_check():

    from newspaper import Article
    from bs4 import BeautifulSoup

    url = 'http://aqicn.org/city/vietnam/ho-chi-minh-city/us-consulate/'
    article = Article(url)
    article.download()
    mydoc = article.html

    soup = BeautifulSoup(mydoc, 'html.parser')

    polvalue = soup.find('div', attrs={'class' : 'aqivalue'}).text
    #print(polvalue)

    poltime= soup.find('span', attrs={'id' : 'aqiwgtutime'}).text
    #print(poltime)

    return [polvalue, poltime]