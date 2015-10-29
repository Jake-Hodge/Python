import twitter, datetime

#Load in keys, secrets etc into an array
file = open("TwitterCredentials.txt")
creds = file.readline().strip().split(',')

#/Users/J-Mac/Library/Application Support/Google/Chrome/Default
#/Users/J-Mac/Library/Application\ Support/Google/Chrome/Default/Current\ Session 
history = open("/Users/J-Mac/Library/Application Support/Google/Chrome/Default/Current Session")

histFull = history.read()



print(histFull)
#Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(creds[0], creds[1],creds[2],creds[3])


""" TO DO:
find http
find slash
convert url to page title
"""
