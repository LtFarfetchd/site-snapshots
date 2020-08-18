from urllib.request import Request, urlopen
from snapshotBuilder import buildSnapShotFromHtml

# read out the list of necessary sites
sites = [site for site in open('sites.config').readlines()]

# hit the site and store the html, converted to snapshot
cachedContent = {}
for site in sites:
    response = urlopen(Request(site, headers={'User-Agent': 'Mozilla/5.0'}))
    cachedContent[site] = buildSnapShotFromHtml(response.read())
    print(cachedContent[site])

# build a snapshot from the html


# determine if a snapshot exists


    # if no: build one and write it to file

    # if yes: compare it to the new cached one

        # if same: notify unchanged

        # if different: notify changed