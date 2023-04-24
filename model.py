import os
os.environ["OPENAI_API_KEY"] = ""


from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains.question_answering import load_qa_chain

from doc import loadPath, loadDocs

loaders = loadPath('../doc')
docs = loadDocs(loaders)

index = VectorstoreIndexCreator().from_loaders(loaders)
llm = OpenAI(temperature=0.9)
chain = load_qa_chain(llm, chain_type="stuff")

def run(query):
    return chain.run(input_documents=docs, question=query)
