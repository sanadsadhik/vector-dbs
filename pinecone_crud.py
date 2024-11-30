from pinecone import Pinecone, ServerlessSpec
from config import PINECONE_API_KEY

api_key = PINECONE_API_KEY
pc = Pinecone(api_key=PINECONE_API_KEY)

# to list all the indexes
# print(pc.list_indexes())

pc.create_index(
    name="crud",
    dimension=3,
    spec=ServerlessSpec(    
        cloud="aws",
        region="us-east-1"
    )
)

idx = pc.Index("crud") # pointer to the index

# upsert
data = [('vec1',[1.0,2.0,3.0]), ('vec2',[11.0,12.0,13.0]), ('vec3',[31.0,32.0,33.0])] 
# data is going to be a list of tuples
# in each tuple - first element is vector id and second is the list of vectors
idx.upsert(data)

# update
idx.update(id="vec3",values=[0.55,0.55,0.55])

# query
print(idx.query(vector=[0,0,0],top_k=1,include_values=True))

# fetch by id
print(idx.fetch(ids=["vec1"]))
print(idx.fetch(ids=["vec1","vec3"]))

# delete
idx.delete(ids=["vec3"])
idx.delete(delete_all=True)