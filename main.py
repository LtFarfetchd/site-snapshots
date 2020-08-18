from urllib.request import Request, urlopen
from snapshotBuilder import buildSnapShotFromHtml
from os import path

# read out the list of necessary sites
sites = [site.strip() for site in open('sites.config').readlines()]
excludedElementTypes = [elementType.strip() for elementType in open('excludedElems.config').readlines()]

# hit the site and store the html, converted to snapshot
cachedContent = {}
for site in sites:
    response = urlopen(Request(site, headers={'User-Agent': 'Mozilla/5.0'}))
    cachedContent[site] = buildSnapShotFromHtml(response.read(), excludedElementTypes)

for site, cachedSnap in cachedContent.items():
    filename = f'snapshots/{site[site.rindex("//")+2:site.index(".")]}.snap'
    with open(filename, mode='r+' if path.exists(filename) else 'w+') as snapshot:
        snapshotContents = snapshot.read()
        if len(snapshotContents) == 0:
            snapshot.write(cachedSnap)
            print(f'New site: {site}')
        else:
            if (cachedSnap != snapshotContents):
                snapshot.truncate(0)
                snapshot.seek(0)
                snapshot.write(cachedSnap)
                print(f'Changed site: {site}')