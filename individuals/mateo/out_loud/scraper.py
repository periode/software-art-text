# ====| OUT/LOUD - Web Scraper |====

import requests
import bs4
import json
import sys
import getopt
import random

numQ = 10
numA = -1
outStr = "test"
tag = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "hq:a:o:t:")
except getopt.GetoptError:
    print("WRONG OPTION (-h for help)")
    sys.exit()

for opt, arg in opts:
    if opt == '-q':
        numQ = int(arg)
    elif opt == '-a':
        numA = int(arg)
    elif opt == '-o':
        outStr = str(arg)
    elif opt == '-t':
        tag = str(arg)
    elif opt == '-h':
        print("""HELPITY HELP:
        -q [num]  : Number of questions
        -a [num]  : Number of answers
        -o [name] : Name of output json file""")
        sys.exit()

def parse(txt):
    return bs4.BeautifulSoup(txt, "html.parser")


baseURL = "https://stackoverflow.com"
firstURL = ""
firstURL += baseURL

if tag is not None:
    firstURL += "/questions/tagged/" + tag
    outStr += "_" + tag
    print("TAG:", tag)

baseReq = requests.get(firstURL)
print("Scraping", baseReq.url)

parsedBase = parse(baseReq.text)
questionList = parsedBase.find_all(class_='question-summary')
print("Page has a list of", len(questionList), "questions")

output = {
        "questions": [],
        "answers": []
    }

with open(outStr + '.json', 'w') as oFile, open(outStr + '.txt', 'w') as oTxt:
    done = False

    for q in questionList:
        qLink = q.find('a')['href']
    
        qReq = requests.get(baseURL + qLink)

        parsedQ = parse(qReq.text)
        qText = parsedQ.find(id="question").find(class_='post-text')
        aList = parsedQ.find_all(class_="answer")

        if len(aList) == 0:
            continue

        qPar = []
        for p in qText.find_all('p'):
            qPar.append(p.text)

        output['questions'].append(qPar)

        for ans in aList:
            txt = ans.find(class_="post-text")
            
            ansGroup = []

            for p in txt.find_all('p'):
                ansGroup.append(p.text)

            output['answers'].append(ansGroup)

            if len(output['answers']) >= numA and numA > 0:
                done = True
                break

        if (len(output['questions']) >= numQ and numA < 1) or done:
            break
        
    print("Writing to JSON...")
    oText = json.dumps(output)
    oFile.write(oText)

    print("Generating randomized dialogue...")
    for i in range(10):
        oTxt.write("\nQUESTION:\n")
        curQ = '\n'.join(random.choice(output['questions']))
        oTxt.write(curQ)
        oTxt.write('\nANSWERS:\n')
        j = 0
        count = 0
        while j < 3 and count < 100:
            try:
                curArr = random.choice(output['answers'])
                curA = random.choice(curArr)
                oTxt.write(curA + '\n\n')
                j += 1
            except IndexError:
                continue
            count += 1

    print("All done!")        