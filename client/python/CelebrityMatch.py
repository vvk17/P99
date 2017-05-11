import sys
import math
import requests
import json
import operator
import twitter
#import script as pi
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

#This function is used to receive and analyze
#the last 200 tweets of a Twitter handle using
#the Watson PI API

def analyze(handle):

  #The Twitter API credentials
  twitter_consumer_key = 'HwhwHpy4WyOWigCmObQE5DWVU'
  twitter_consumer_secret = 'lGXgjNDiWa5lMx2QdztWi6ZtwBs8DsaUlrHUPZXzo4QMmjIzEX'
  twitter_access_token = '743533649862103042-gB6KZ2eiqcyWYIxw5mBbOcB0fD9R120'
  twitter_access_secret = 'hesbvKtV6aoaj9nMUh4SNTiqZbYxdnroPwjjxFoKOCk38'

  #Invoking the Twitter API
  twitter_api = twitter.Api(consumer_key=twitter_consumer_key,consumer_secret=twitter_consumer_secret,access_token_key=twitter_access_token,access_token_secret=twitter_access_secret)

#Retrieving the last 200 tweets from a user
  statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

#Putting all 200 tweets into one large string called "text"
  #Putting all 200 tweets into one large string called "text"
  text = ""

  for s in statuses:
#    print "status is", s.text
    if (s.lang =='en'):
          text += s.text.encode('utf-8')

 #   print text


  #Analyzing the 200 tweets with the Watson PI API
  pi_result = PersonalityInsights(username='002b8c93-6fdd-43a3-89a4-78960dff5301', password='5gM5O1n6Fyis').profile(text)

  #Returning the Watson PI API results
  return pi_result

#This function is used to flatten the result
#from the Watson PI API
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data

#This function is used to compare the results from
#the Watson PI API
def compare(dict1, dict2):
  compared_data = {}
  for keys in dict1:
        if dict1[keys] != dict2[keys]:
          compared_data[keys] = abs(dict1[keys] - dict2[keys])
  return compared_data

def get_twitter_id (who) :
  twitter_id = raw_input ("Enter twitter id of "+who+" : ")
  print twitter_id

  return twitter_id

#The two Twitter handles
#user_handle = "@V12345Valery"
user_handle = get_twitter_id("you")
#celebrity_handle = "@CharlizeAfrica"
celebrity_handle = get_twitter_id("celebrity")

#Analyze the user's tweets using the Watson PI API
user_result = analyze(user_handle)
print user_result
celebrity_result = analyze(celebrity_handle)

#Flatten the results received from the Watson PI API
user = flatten(user_result)
print user
celebrity = flatten(celebrity_result)

#Compare the results of the Watson PI API by calculating
#the distance between traits
compared_results = compare(user,celebrity)

#Sort the results
#sorted_results = compared_results.items()
sorted_results = sorted(compared_results.items(), key=operator.itemgetter(1))

#Print the results to the user
for keys, value in sorted_results[:50]:
  print repr(keys).rjust(25),' | {0:5.1f}% | {1:5.1f}% | {2:5.1f}%'.zfill(4).format(user[keys]*100,celebrity[keys]*100,compared_results[keys]*100)
#  print keys ,
#  print (user[keys]),
#  print (' | -> '),
#  print ('{0:3f}%'.format(celebrity[keys]*100)),
#  print (' -> '),
#  print (compared_results[keys])
