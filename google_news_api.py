from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

def get_news():
    googlenews=GoogleNews(start='05/17/2020',end='05/10/2020')
    googlenews.search('itc share')
    result=googlenews.result()
    df=pd.DataFrame(result)
    print(df.head())

get_news()