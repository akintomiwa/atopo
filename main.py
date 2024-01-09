import os
import logging
from datetime import datetime, timezone
import sys
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
# from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper

from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from source.sysclass import XCorpus, ThematicAnalysis

# from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import numpy as np
# import matplotlib.pyplot as plt
# import random
# from scipy import stats
import seaborn as sns
from dataclasses import dataclass
from random import seed, randint
from fileinput import close
from posixpath import split
import string
string.punctuation
import re
import nltk
from nltk.tokenize import word_tokenize
from ekphrasis.classes.segmenter import Segmenter 

# run once , post imports 
# nltk.download('stopwords')
# nltk.download('punkt')

from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened

load_dotenv()
OPENAI_MODEL = "gpt-3.5-turbo"
# OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# X_BEARER_TOKEN = os.environ.get("X_BEARER_TOKEN")
X_API_KEY = os.environ.get("X_API_KEY")
X_API_SECRET = os.environ.get("X_API_SECRET")
X_ACCESS_TOKEN = os.environ.get("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.environ.get("X_ACCESS_TOKEN_SECRET")

# def retrieve_user_posts(username):
#     # Main query
#     query = f"from:{username} -is:retweet"
#     optional = f"--start-time 2023-07-01 --end-time 2022-12-30  --limit 1000 --archive {username}.jsonl"
#     fullquery = str(query + optional)
#     print(f"Full query: {fullquery}")
#     return fullquery

def llm_analysis():
    PROMPT_THEME_INFO = """
    Provide information about the themes and general ideas present in this data {country}.{format_instructions}. 
    Themes can include Politics, Sports, Science, Technology, and Music.
    """
    # V1
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    # for stucturing LLM output 
    parser = PydanticOutputParser(pydantic_object=ThematicAnalysis)
    country = input("Enter the name of a country: ")
    # core 
    message = HumanMessagePromptTemplate.from_template(template=PROMPT_THEME_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(country=country, format_instructions=parser.get_format_instructions())
    try:
        response = llm(chat_prompt_with_values.to_messages())
        data = parser.parse(response.content)

        print(f"The major themes in {data.username}'s post archive include: ")
        print(f"Theme 1: {data.theme1}. Keywords:  {data.theme1kw}")
        print(f"Theme 2: {data.theme2}. Keywords:  {data.theme2kw}")
        print(f"Theme 3: {data.theme3}. Keywords:  {data.theme3kw}")
    except Exception as e:
        print(f"Failure to fetch response from LLM: {e}")
    pass

# using prompt and chat llm model 
def main():
    """
    Main program
    """
    # Set today's date as string
    date_str = str(datetime.today())

    # Set data, log path 
    # DATA_PATH = os.environ.get("DATA_PATH")
    LOG_PATH = os.environ.get("LOG_PATH")

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %I:%M:%S%p',
        filename=LOG_PATH + date_str[0:10] + '_' + '_app.log',
    )
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)
    logging.info('Log Started')

    logging.info(f"\nToday's date is: {str(datetime.today())}.")

    x = Twarc2(bearer_token="X_BEARER_TOKEN")

    # x = Twarc2(consumer_key= X_API_KEY,
    #            consumer_secret= X_API_SECRET,
    #            access_token= X_ACCESS_TOKEN,
    #            access_token_secret= X_ACCESS_TOKEN_SECRET
    #            )

    # fetch username 
    # username = input("Enter your X username: ")
    username = os.environ.get("DEFAULT_USERNAME")
    print(f"Target username: {username}")

    
    # start date
    date_string = "2022-01-30"

    # Convert to datetime object
    date_object = datetime.strptime(date_string, "%Y-%m-%d")

    # Set the timezone to UTC
    start_time = date_object.replace(tzinfo=timezone.utc)
    # end_time = datetime.today()
    
    # Get the current date and time in UTC - use as end time
    end_time = datetime.now(timezone.utc)


    # search_results is a generator, max_results is max tweets per page, 100 max for full archive search with all expansions.
    search_results = x.search_all(query=f"{username} lang:en -is:retweet", start_time=start_time, end_time=end_time, max_results=100)

    # Get all results page by page:
    for page in search_results:
        # Do something with the whole page of results:
        # print(page)
        # or alternatively, "flatten" results returning 1 tweet at a time, with expansions inline:
        for tweet in ensure_flattened(page):
            # Do something with the tweet
            print(tweet)

        # Stop iteration prematurely, to only get 1 page of results.
        break

    if search_results:
        print(len(search_results))

    # # construct full query 
    # fullquery = retrieve_user_posts(username=username)
    
    # # retrieve posts from SM service with twarc2 CLI 
    # try:
    #     # os.system(f"twarc2 search " + "{fullquery}")
    #     all = f"twarc2 search {fullquery}"
    #     print(f"Full CLI command: {all}")
    #     # os.system("twarc2 search " + fullquery)
    #     os.system(all)
    #     # # flatten
    #     # os.system(f"twarc2 flatten {username}_tweets.jsonl {username}_flattweets.jsonl")
    #     # # export to csv
    #     # os.system(f"twarc2 csv {username}_flattweets.jsonl {username}_flattweets.csv") 
    # except Exception as e:
    #     print(f"Error fetching tweets with twarc. Error:{e}")
    # try:    
    #     # read in csv file
    #     df_cur= pd.read_csv("{username}_flattweets.csv")
    #     print(df_cur.head())
    #     # make Corpus object 
    #     user_corpus = XCorpus(df_cur)
    #     print("User Corpus initialized.")
    #     print(f" Corpus Id: {user_corpus.id}. Username {user_corpus.username}")
    # except Exception as e:
    #     print(f"Error reading in posts csv. Error:{e}")

 
    
    # if user_corpus is not None:
    #     llm_analysis()


if __name__ == "__main__":
    main()