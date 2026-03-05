import pandas as pd


#  select boyicha 4-masala, article_view
data = {
    'article_id': [1,1,2,2,4,3,3],
    'author_id' : [3,3,7,7,7,4,4],
    'viewer_id' : [5,6,7,6,1,4,4],
    'view_date' : ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21', '2019-07-21']
}

df = pd.DataFrame(data)
result = pd.DataFrame({'id': sorted(df[df['author_id'] == df['viewer_id']]['author_id'].unique())})

#  select boyicha 5-masala, invalid_tweets
data = {
    'tweet_id': [1,2],
    'content': ['Let us Code', 'More than fifteen chars are here!']
}
df = pd.DataFrame(data)
result =pd.DataFrame({'tweet_id': (df[df['content'].str.len() > 15][['tweet_id']])})