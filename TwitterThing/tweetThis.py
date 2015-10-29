import twitter, datetime

#Hardcode a user ID into a var
user = 15439395

#Load in keys, secrets etc into an array
file = open("TwitterCredentials.txt")
creds = file.readline().strip().split(',')
    
#Create a new API wrapper, passing in my credentials one at a time
api = twitter.Api(creds[0], creds[1],creds[2],creds[3])

#Gets the moste recent batch of status updates
statuses = api.GetUserTimeline(user)

#print out most recent one
print (statuses[0].text)