import os
from langchain import OpenAI
os.environ["OPENAI_API_KEY"] = ""

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from doc import loadPath, loadDocs

loaders = loadPath('../doc')
text_splitter = SpacyTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(loadDocs(loaders))


embeddings = OpenAIEmbeddings()

vectorstore = ElasticVectorSearch.from_documents(documents, embeddings, elasticsearch_url="https://elastic:passw0rd@dsm.local:9200")

chain = load_qa_with_sources_chain(OpenAI(temperature=0.9), chain_type="stuff")

# query = "What did the president say about Justice Breyer"

def ask(query):
    resources = vectorstore.similarity_search(query)
    return chain({"input_documents": resources[:1], "question": query})
