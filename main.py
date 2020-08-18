from urllib.request import Request, urlopen
from snapshotBuilder import buildSnapShotFromHtml

# read out the list of necessary sites
sites = [site.strip() for site in open('sites.config').readlines()]
excludedElementTypes = [elementType.strip() for elementType in open('excludedElems.config').readlines()]

# hit the site and store the html, converted to snapshot
cachedContent = {}
for site in sites:
    response = urlopen(Request(site, headers={'User-Agent': 'Mozilla/5.0'}))
    cachedContent[site] = buildSnapShotFromHtml(response.read(), excludedElementTypes)

for site, cachedSnap in cachedContent.items():
    with open(f'snapshots/{site[site.rindex("//")+2:site.index(".")]}.snap', mode='w+') as snapshot:
        snapshotContents = snapshot.read()
        if len(snapshotContents) == 0:
            print(f'New site: {site}')
            snapshot.write(cachedSnap)
        else:
            if (cachedSnap != snapshotContents):
                print(f'Changed site: {site}')
                snapshot.write(cachedSnap)