import chromadb
import pandas as pd

df = pd.read_csv('medium_post_titles.csv')

df = df.dropna()
df = df[~df["subtitle_truncated_flag"]]

topics_of_interest = ['artificial-intelligence','data-science','machine-learning']
topics_of_interest = ['data-science']

df = df[df['category'].isin(topics_of_interest)]

df['text'] = df['title'] + df['subtitle']

df['meta'] = df.apply( lambda x: {
    'text': x['text'],
    'category': x['category']
},axis=1)

# print(df.head(2))

chroma_client = chromadb.Client() # in memory database

#collection creation
article_collection = chroma_client.create_collection(name='medium-article')
# if we do not specify embeddings, then chromadb will use it own default embedding model

#inserting data
article_collection.add(
    ids=[f"{x}" for x in df.index.tolist()],
    documents=df['text'].tolist(),
    metadatas=df['meta'].tolist()
)

# article_collection.delete() to delete the collection