from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
from datetime import date, timedelta

def get_news():
    current_date = date.today().strftime("%m/%d/%Y")
    end_date = date.today() - timedelta(days=7)
    end_date = end_date.strftime("%m/%d/%Y")
    # print(current_date, end_date)
    googlenews=GoogleNews(current_date, end_date)
    googlenews.search('itc share')
    result=googlenews.result()
    df=pd.DataFrame(result)
    print(df.head())

get_news()