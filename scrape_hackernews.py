import requests
from bs4 import BeautifulSoup
import pprint

# Send GET request to the Hacker News homepage and parse the HTML content
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# Select all links and subtext for articles on the homepage
links = (soup.select('.titleline > a'))
subtext = soup.select('.subtext')

# Send GET request to page 2 of the Hacker News homepage and parse the HTML content
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# Select all links and subtext for articles on page 2
links2 = (soup2.select('.titleline > a'))
subtext2 = soup2.select('.subtext')

# Combine links and subtexts from both pages
megalinks =  links + links2
megasubtexts = subtext + subtext2

# Define function to sort list of articles by number of votes
def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

# Define function to create a list of articles with their title, link, and number of votes
def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

# Call the 'create_custom_hn' function with the combined links and subtexts and print the resulting list of articles with pprint
pprint.pprint(create_custom_hn(megalinks,megasubtexts))
