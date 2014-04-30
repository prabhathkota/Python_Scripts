import twitter
import requests
# api = twitter.Api()
# statuses = api.GetPublicTimeline()
# print [s.user.name for s in statuses]


url = 'http://search.twitter.com/search.json?q=johnboehner'
results = requests.get(url)
 
better_results = results.json()

print better_results

#for post in better_results['results']:
#    print post['text'].encode('utf-8')