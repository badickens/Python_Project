'''
Using a text file containing the stock symbols - symbol.txt
'''


import urllib.request
import re
import time

symbolFile = open("symbols.txt")

symbolsList = symbolFile.read()
newSymbolsList = symbolsList.split('\n')

i = 0
while i < len(newSymbolsList):

    url = "http://finance.yahoo.com/q?s=" +newSymbolsList[i] +"&ql=1"  # makes url string to search for each stock on yahoo
    print(url)

    htmlfile = urllib.request.urlopen(url)  # 
    htmltext = str(htmlfile.read())
    print(htmltext[:2000])
    #regex =  '<span id="yfs_184_[^.]*">(.+?)</span>'
    pattern = re.compile('<span id="yfs_184_[^.]*">(.+?)</span>')
    price = pattern.findall(htmltext[:2000])  	

    time.sleep(5)   # pause 5 seconds

    print("the price of", newSymbolsList[i], " is ", price)   
    i += 1		

'''
b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
\n<html lang="en-US">\n<head>\n<title>AAPL: Summary for Apple Inc.- Yahoo! Finance</title>\n
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"><meta name="description"
xml:space="default" content="View the basic AAPL stock chart on Yahoo! Finance.
Change the date range, chart type and compare Apple Inc. against\nother companies.">
<meta name="keywords" content="AAPL, Apple Inc., AAPL stock chart, Apple Inc. stock chart,
stock chart, stocks, quotes, finance"><meta property="fb:app_id" content="118155468215844">
<meta property="fb:admins" content="503762770,100001149693905"><meta property="og:type"
content="company"><meta property="og:site_name" content="Yahoo! Finance"><meta property="og:title"
content="Apple Inc."><meta property="og:image" content="http://l.yimg.com/a/p/fi/31/09/00.jpg">
<meta property="og:url" content="http://finance.yahoo.com/q?s=AAPL"><meta property="og:description"
content="View the basic AAPL stock chart on Yahoo! Finance. Change the date range, chart type and
compare Apple Inc. against\nother companies."><link rel="canonical" href="http://finance.yahoo.com/q?s=AAPL">
<script>\n          window.yfinBucket = \'\';\n        </script>\n<link rel="stylesheet"
href="http://l.yimg.com/zz/combo?kx/yucs/uh3/uh/1132/css/uh_non_mail-min.css&amp;
kx/yucs/uh3s/atomic/63/css/atomic-min.css&amp;kx/yucs/uh_common/meta/3/css/meta-min.css&amp;
kx/yucs/uh3/top-bar/366/css/no_icons-min.css&amp;kx/yucs/uh3/search/css/588/blue_border-min.css&amp;
kx/yucs/uh3/get-the-app/151/css/get_the_app-min.css&amp;
bm/lib/fi/common/p/d/static/css/2.0.356981/2.0.0/mini/yfi_quote_summary_lego_concat.css&amp;
bm/lib/fi/common/p/d/static/css/2.0.356981/2.0.0/mini/yfi_symbol_suggest.css&amp;
bm/lib/fi/common/p/d/static/css/2.0.356981/2.0.0/mini/yui_helper.css&amp;
bm/lib/fi/common/p/d/static/css/2.0.356981/2.0.0/mini/yfi_theme_teal.css&amp;
bm/lib/fi/common/p/d/static/css/2.0.356981/2.0.0
'''
