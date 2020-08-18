from bs4 import BeautifulSoup

def buildSnapShotFromHtml(htmlDocument, excludedElems=[]):
    soup = BeautifulSoup(htmlDocument, 'html5lib')
    for elementType in excludedElems:
        for element in soup(elementType):
            element.decompose()
    body = soup.find('body').prettify()
    return body