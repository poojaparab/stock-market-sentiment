import requests
import pandas as pd
import json
import ast
import yaml

def create_twitter_url(stock_name):
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query={}".format(stock_name)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        mrf, q
    )
    return url
def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]

def process_yaml():
    with open(".\cred\config.yaml") as file:
        return yaml.safe_load(file)

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def main():
    stock_name = "itc share"
    url = create_twitter_url(stock_name)
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    res_json = twitter_auth_and_connect(bearer_token, url)
    print(res_json)

main()