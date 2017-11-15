import requests

target_url = "http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"

req = requests.get(target_url)

print "getting url: %s" % target_url
if req.status_code == 200:
    print "got result!"
    print req.text
else:
    print "something went wrong, response code %i" % req.status_code
