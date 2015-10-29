""" THIS WEEK'S PRACTICAL

    In the next practical you will create an interactive chatbot.
    This should engage the user in interesting and intelligent conversation.
    The bot should be able to ask and answer questions.
    Try to make it as realistic and life-like as possible.

    Don't use any existing natural language processing libraries.
    It's more important to try out the features of Python to create your bot.

    Not all of the information you require is in this lecture !
    You will have to use your initiative (and a search engine ;o)

    There are a number of string functions that will be useful
         (raw_input, find, replace, split, upper, lower)

    You might like to use this list of "stop words" to help in your task:

        http://www.ranks.nl/stopwords """



# Import some things
import random  
        
from stop_words import get_stop_words

stopWords = get_stop_words('english')
"""for word in stopWords:
    print (word) """ # For testing
    
    # Lists of positive, negative and greeting responses
posWords = ['well', 'fine', 'good', 'alright', 'great', 'excellent', 'fantastic' ]
negWords = ['bad', 'rubbish', 'poorly', 'unwell', 'dying', 'not']
greetings = ['Hi', 'Hello', 'Howdy', 'Hola', 'Greetings', 'Hey', 'Yo']
rand_greeting = random.choice(greetings)
print rand_greeting

 
"""def nameFunc():
    
    for word in stopWords:
        if word in stopWords:
            print (word)
        elif (word) != name:
         print name 
        else:
            print (word) """
            
"""def nameFunc():
        if any(stopWords in word for word in name):
                   print word """
            

name = raw_input(">>> What is your name? ").lower()
name = " " + name + " "
name = name.replace(" name "," ")
name = name.replace(" called "," ")
nameArray = name.split()   # splits each string into an array/list
for word in nameArray:
    if word in stopWords:
        name = name.replace(" " + word + " "," ") # removes any words in the userinput string that matches stopwords
        print("removed: " + word)
        
        
name = name.title() #Capitalizes the first char of name 
wellbeing = raw_input("Hello" + name + ", " + "How are you? >>> ").lower()  
wellArray = wellbeing.split()
for word in wellArray:
    if word in stopWords:
        wellbeing = wellbeing.replace(" " + word + " "," ")
    if word in posWords:
        print "Thats good to hear"
    elif word in negWords:
        print "Aw, what a shame"
    #else:
     #   print "I don't know if thats good or bad :/"

""" If the ELSE is left in it will print out the string everytime it runs
  through a word that isnt in the pos/neg list. Remove the stopwords first, then
  the only words left should be the pos or neg word"""
 










