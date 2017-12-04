# ====| OUT/LOUD - Web Scraper |====

import requests
import bs4
import json
import sys
import getopt

numQ = 10
numA = -1
outStr = "test"

try:
    opts, args = getopt.getopt(sys.argv[1:], "hq:a:o:")
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
    elif opt == '-h':
        print("""HELPITY HELP:
        -q [num]  : Number of questions
        -a [num]  : Number of answers
        -o [name] : Name of output json file""")
        sys.exit()

def parse(txt):
    return bs4.BeautifulSoup(txt, "html.parser")


baseURL = "https://stackoverflow.com"

baseReq = requests.get(baseURL)
print("Scraping", baseURL)

parsedBase = parse(baseReq.text)
questionList = parsedBase.find_all(class_='question-summary')

output = {
        "questions": [],
        "answers": []
    }

with open(outStr + '.json', 'w') as oFile:
    done = False

    for q in questionList:
        qLink = q.find('a')['href']
    
        qReq = requests.get(baseURL + qLink)

        parsedQ = parse(qReq.text)
        qText = parsedQ.find(id="question").find(class_='post-text')
        aList = parsedQ.find_all(class_="answer")

        if len(aList) == 0:
            continue

        print("QUESTION")

        qPar = []
        for p in qText.find_all('p'):
            qPar.append(p.text)

        print(qPar)
        output['questions'].append(qPar)

        print("ANSWERS")
        for ans in aList:
            txt = ans.find(class_="post-text")
            print(txt.prettify())
            output['answers'].append(txt.text)

            if len(output['answers']) >= numA and numA > 0:
                done = True
                break

        if (len(output['questions']) >= numQ and numA < 1) or done:
            break
        
    print("Writing to JSON...")
    oText = json.dumps(output)
    oFile.write(oText)
    print("All done!")        