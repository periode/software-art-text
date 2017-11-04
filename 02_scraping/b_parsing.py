import requests
from bs4 import BeautifulSoup

target_url = "http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"

req = requests.get(target_url)

def parse(content):
    soup = BeautifulSoup(content, "html.parser")
    all_deceased = soup.find_all("tr")
    for deceased in all_deceased:
        print "went by the name %s %s" % (deceased.contents[9].string.strip(), deceased.contents[7].string.strip())

print "getting url: %s" % target_url
if req.status_code == 200:
    print "got result!"
    parse(req.text)
else:
    print "something went wrong, response code %i" % req.status_code
