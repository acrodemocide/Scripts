from urllib.request import urlopen
import sys

if (len(sys.argv) < 2):
    print('Need more command line args (WebRequest <url>)')
else:
    url = sys.argv[1]
    response = urlopen(url)
    webContent = response.read()
    # print(webContent[0:300])
    print(webContent)