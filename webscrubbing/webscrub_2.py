'''
Refactoring webscrub_1.py with more direct reg ex code
'''


import urllib.request
import re

urls = ["https://google.com", "http://vox.com", "http://readwrite.com"]

i = 0
   
pattern = re.compile(r'<title>(.+?)</title>')


while i < len(urls):
    htmlfile = urllib.request.urlopen(urls[i])
    htmltext = str(htmlfile.read())
    print(htmltext[:500])
    titles = pattern.findall(htmltext[:500])	# each title for each chunk of htmltext as a string
    print('\n\n')
    print(titles)
    print("---***---***---***---***---***---***---***---***---")   # url separator
    i += 1	

'''
google.com output:
b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage"
lang="en"><head><meta content="Search the world\'s information, including
webpages, images, videos and more. Google has many special features to help
you find exactly what you\'re looking for." name="description"><meta content="noodp"
name="robots"><meta content="/images/google_favicon_128.png" itemprop="image">
<title>Google</title><script>(function(){window.google={kEI:\'3SLaVaSnFsKqNtaygZAM\',
kEXPI:\'3700243,3700372,40298
'''
