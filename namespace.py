from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY
import numpy as np

api_key = PINECONE_API_KEY
pc = Pinecone(api_key=PINECONE_API_KEY)

idx = pc.Index("crud") # pointer to the index

dimensions = 3

# count of emails
emails_with_subject = 20
emails_with_body = 45
emails_with_others = 45

# creating dummy vectors, assume embedded
vects_subject = np.random.rand(emails_with_subject,dimensions).tolist()
# tolist() is to convert the numpy object to python list
vects_body = np.random.rand(emails_with_body,dimensions).tolist()
vects_others = np.random.rand(emails_with_others,dimensions).tolist()

# create ids for the above vects
ids_subject = map(str, np.arange(emails_with_subject).tolist())
ids_body = map(str, np.arange(emails_with_body).tolist())
ids_others = map(str, np.arange(emails_with_others).tolist())
# ids in pinecone should be a string

# zip id and vects
vectors_subject = list(zip(ids_subject,vects_subject))
vectors_body = list(zip(ids_body,vects_body))
vectors_others = list(zip(ids_others,vects_others))

# default namespace is ""
idx.upsert(vectors_subject,namespace='subject')
idx.upsert(vectors_body,namespace='body')
idx.upsert(vectors_others,namespace='others')





