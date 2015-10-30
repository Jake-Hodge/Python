import twitter, datetime

#Load in keys, secrets etc into an array
file = open("TwitterCredentials.txt")
creds = file.readline().strip().split(',')

#Create a new API wrapper, passing in credentials one at a time
api = twitter.Api(creds[0], creds[1],creds[2],creds[3])

#Find out current time
timeNow = datetime.datetime.utcnow()

history = open("/Users/J-Mac/Library/Application Support/Google/Chrome/Default/Current Session")
histFull = history.read()

first = "https://"
second = "/"

# Starts from the beginning of txt file and goes in order
"""start = histFull.find(first) + len(first) 
finish = histFull.find(second, start)"""

#Starts at the end of txt file and works in reverse. Makes sense to use this one, as bottom of
#text file is the most recent page.
finish = histFull.rfind(second)
start = histFull.rfind(first, 0, finish - len(first)) + len(first)
latestSite = (histFull[start:finish])
print(latestSite)


#Post status update and get response for Twitter
twitResponse = api.PostUpdate("I recently visited " + latestSite)
#Print out response text (should be the status update if everything worked)
print("Status updated to: " + twitResponse.text)




""" TO DO:
find http (look up Find on Python docs)
find slash
convert url to page title
"""
