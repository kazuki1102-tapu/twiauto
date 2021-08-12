#!/opt/alt/python36/bin/python3.6

from requests_oauthlib import OAuth1Session

# -*- coding: utf-8 -*-
import cgi
import sys
import io
import csv
import random

import schedule
import time


#key
CK = 'RNga9GnDLq5f7K2PKTArzC6iD'
CS = '8h8XnpXQtAlHLsfZKoFAWdaks529IiS8x80IXBD1shv6zeanTD'
AT = '1260734060621524993-hTD5mbO0rz8Vj8TicJ9pT2jBn7gBkD'
AS = 'wUxDzRSm2b7z7ciSv5jkEaNP51Wgbd2ahLppbJnQBe2XT'

def tweet():
  twitter = OAuth1Session(CK,CS,AT,AS)
  
  url = 'https://api.twitter.com/1.1/statuses/update.json'
  tweetText = getTweetContentsFromCsv()
  params = {'status': tweetText}

  response = twitter.post(url, params = params)
  print(response.status_code)

def getTweetContentsFromCsv():
    with open('C:/wps_Excel/python_training/tweetContents.csv',"r") as f:
        tweetContents = list(csv.reader(f))

    tweetContentsLength = len(tweetContents)        
    randomNum = random.randrange(tweetContentsLength)
    getTweetContent = tweetContents[randomNum]
    print(getTweetContent)
    
    return getTweetContent

def main():
    schedule.every(12).hour.do(tweet)
    schedule.run_pending()

    while True:
        schedule.run_pending()

if __name__ == "__main__":
    main()    