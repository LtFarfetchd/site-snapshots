from bs4 import BeautifulSoup

def buildSnapShotFromHtml(htmlDocument):
    soup = BeautifulSoup(htmlDocument, 'html5lib')
    body = soup.find('body').prettify()
    return body