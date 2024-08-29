from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv

load_dotenv()
# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

## Setting env Variable
os.environ['PINECONE_API_KEY'] = os.getenv("PINECONE_API_KEY")
os.environ['HF_API_TOKEN'] = os.getenv("HF_TOKEN")
    
print("Import Successfully")

def pinecone_config():
    #configuring pinecone database
    document_store = PineconeDocumentStore(
            index="default",
            namespace="default",
            dimension=768,
            spec={"serverless": {"region": "us-east-1", "cloud": "aws"}}
        )
    return document_store