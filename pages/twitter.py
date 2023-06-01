# from sklearn.model_selection import train_test_split
import os
import pandas as pd
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy import stats
from random import seed
from random import randint
import seaborn as sns
from dataclasses import dataclass
from fileinput import close
from posixpath import split
import string
string.punctuation
import re
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize
from apikey import TWITTER_BEARER_TOKEN, TWITTER_API_KEY, TWITTER_API_SECRET
import datetime
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened

# authentication
os.environ['TWITTER_API_KEY'] = TWITTER_API_KEY
os.environ['TWITTER_API_SECRET'] = TWITTER_API_SECRET
os.environ['TWITTER_BEARER_TOKEN'] = TWITTER_BEARER_TOKEN

# twarc2 configure

# Main query
# !twarc2 search "flood OR climate OR heat OR rain OR climate change OR cop26 from:OlumideIdowu -is:retweet"  --start-time 2022-01-01 --end-time 2022-06-30  --limit 1000 --archive Olumide_tweets.jsonl
# flatten
# !twarc2 flatten Olumide_tweets.jsonl flattened_Olumide_tweets.jsonl



def run_search(query):
    # configure twarc
    t = Twarc2(bearer_token= TWITTER_BEARER_TOKEN)

    # Start and end times must be in UTC
    start_time = datetime.datetime(2020, 3, 21, 0, 0, 0, 0, datetime.timezone.utc)
    end_time = datetime.datetime(2023, 4, 22, 0, 0, 0, 0, datetime.timezone.utc)
    # author_name = "Tomiwa"
    author_username = "akintomiwa_ao"
    query = str("from:" + author_username + " lang:en -is:retweet")
    print(f"Query: {query}")

    # search_results is a generator, max_results is max tweets per page, 100 max for full archive search with all expansions.
    search_results = t.search_all(query=query, start_time=start_time, end_time=end_time, max_results=100)

    # Get all results page by page:
    print(f"Twitter data retrieved")
    # for page in search_results:
    #     # Do something with the whole page of results:
    #     # print(page)
    #     # or alternatively, "flatten" results returning 1 tweet at a time, with expansions inline:
    #     for tweet in ensure_flattened(page):
    #         # Do something with the tweet
    #         print(tweet)

    #     # Stop iteration prematurely, to only get 1 page of results.
    #     break
    print("Tweets retrieved successfully")
    return search_results


