from bs4 import BeautifulSoup

def buildSnapShotFromHtml(htmlDocument, excludedElems=[], excludedClasses=[]):
    soup = BeautifulSoup(htmlDocument, 'html5lib')
    for elementType in excludedElems:
        for element in soup(elementType):
            element.decompose()
    for className in excludedClasses:
        for element in soup.find_all(class_=className):
            element.decompose()
    body = soup.find('body').prettify()
    return body