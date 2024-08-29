from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from QASystem.utils import pinecone_config
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv

load_dotenv()

def ingest(document_store):

    indexing = Pipeline()

    ## Adding the components in pipeline
    indexing.add_component("converter", PyPDFToDocument())
    indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
    indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
    indexing.add_component("writer", DocumentWriter(document_store))

    indexing.connect("converter", "splitter")
    indexing.connect("splitter", "embedder")
    indexing.connect("embedder", "writer")

    indexing.run({"converter": {"sources": [Path("/Users/dhavalantala/Desktop/Q_-_A_Bot_with_Haystack/data/2005.11401v4.pdf")]}})

if __name__ == "__main__":
    
    document_store = pinecone_config()

    ingest(document_store)