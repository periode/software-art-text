import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
our_request = requests.get("http://www.icechewing.com/viewforum.php?f=1", headers = headers)
print our_request.status_code


parsed_html = bs4.BeautifulSoup(our_request.text, "html.parser")

all_results = parsed_html.find_all(class_="topictitle")

#print parsed_html.prettify()

comments = []

for single_result in all_results:
	link = single_result['href']
	new_link = link.replace('./', 'http://www.icechewing.com/')
	topic_request = requests.get(new_link, headers = headers)
	parsed_topic = bs4.BeautifulSoup(topic_request.text, "html.parser")
	topic_results = parsed_topic.find_all(class_="content")

	for result in topic_results:
		print result.text
		sentences = result.get_text().encode('utf-8').split('. ')
		for sentence in sentences:
			
			sentences2 = sentence.split('.')
			for sentence2 in sentences2:

				sentences3 = sentence2.split('! ')
				for sentence3 in sentences3:

					comments.append(sentence3)



saved_comments = open("ice.txt", "w")
for single_comment in comments:
	saved_comments.write(single_comment)
	saved_comments.write("\n")
saved_comments.close()

print "done"
