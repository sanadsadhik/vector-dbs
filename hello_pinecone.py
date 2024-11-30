from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY

api_key = PINECONE_API_KEY
pc = Pinecone(api_key=PINECONE_API_KEY)

# to list all the indexes
# print(pc.list_indexes())

pc.create_index(
    name="test",
    dimension=3,
    spec=ServerlessSpec(    
        cloud="aws",
        region="us-east-1"
    )
) 
# "us-east-1" - for free tier use this region only
print(pc.list_indexes())
