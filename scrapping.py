import requests
from bs4 import BeautifulSoup
import pprint

# Gives the HTML output from the website
resp = requests.get('https://news.ycombinator.com/news')
resp2 = requests.get('https://news.ycombinator.com/?p=2')

# print(resp.text)

# BeautifulSoup allows us to parse

soup = BeautifulSoup(resp.text, "html.parser")
soup2 = BeautifulSoup(resp2.text, "html.parser")

# print(soup) # Output for below becomes a little tidier
# print(soup.body) # Output for body
# print(soup.body.contents) # Output for contents
# print(soup.find_all("div")) # Gives all the div outputs
# print(soup.find_all("a")) # Gives all the 'a' tags
# print(soup.title) # P: <title>Hacker News</title>
# print(soup.find_all("class"))
# print(soup.a) # Gets the 1st 'a' tag that comes up
# print(soup.find("a")) # Does the same as above

# From the page inspect code, look up score and paste id
# print(soup.find(id="score_34507672"))
# <span class="score" id="score_34507672">99 points</span>

# print(soup.select(".score")) # Shows all the scores but with all the info

# print(votes[0].get("id"))       # Grabs the score for the 1st line
links = soup.select(".titleline > a")  # Grabs 1st 'a' tag sitestr
links2 = soup2.select(".titleline > a")  # Grabs 1st 'a' tag sitestr
subtext = soup.select(".subtext")  # Grabs all the scores
subtext2 = soup2.select(".subtext")  # Grabs all the scores

megalinks = links + links2
megasubtext = subtext + subtext2

def sort_stories_by_votes(hackernewslist):
    return sorted(hackernewslist, key= lambda k:k["Votes"], reverse=True)

def create_custom_hackernews(links, subtext):
    hackernews = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace("points", ""))
            if points > 99:
                hackernews.append({"Title": title, "Link": href, "Votes": points})
    return sort_stories_by_votes(hackernews)

# print(create_custom_hackernews(links, subtext))
pprint.pprint(create_custom_hackernews(megalinks, megasubtext))  # Grabs all the titles












