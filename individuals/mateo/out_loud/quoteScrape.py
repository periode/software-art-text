# ====| OUT/LOUD - Quote Scraper |====

import requests
import bs4
import json
import sys
import getopt
import random

outStr = 'quotes'
tag = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "ht:")
except getopt.GetoptError:
    print("WRONG OPTION (-h for help)")
    sys.exit()

for opt, arg in opts:
    if opt == '-t':
        tag = str(arg)
        outStr = tag
    elif opt == '-h':
        print("""HELPITY HELP:
        -q [num]  : Number of questions
        -a [num]  : Number of answers
        -o [name] : Name of output json file""")
        sys.exit()


def parse(txt):
    return bs4.BeautifulSoup(txt, "html.parser")


baseURL = "https://www.brainyquote.com/topics/"

qList = []
if tag is None:
    iReq = requests.get(baseURL + 'inspirational')
    print("Scraping", iReq.url)

    iParsed = parse(iReq.text)
    iList = iParsed.find_all(class_='b-qt')

    mReq = requests.get(baseURL + 'motivational')
    print("Scraping", mReq.url)

    mParsed = parse(mReq.text)
    mList = mParsed.find_all(class_='b-qt')

    qList = mList + iList
else:
    qReq = requests.get(baseURL + tag)
    print("Scraping", qReq.url)
    qParsed = parse(qReq.text)
    qList = qParsed.find_all(class_ = 'b-qt')

random.shuffle(qList)

print("Pages have a list of", len(qList), "quotes")

with open(outStr + '.txt', 'w') as oTxt:
    for quote in qList:
        oTxt.write(quote.text)

    print("All done!") 
