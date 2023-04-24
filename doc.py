from os.path import splitext
from os import listdir
from typing import List
from langchain.document_loaders.powerpoint import UnstructuredPowerPointLoader
from langchain.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain.document_loaders.pdf import UnstructuredPDFLoader
from langchain.document_loaders.base import BaseLoader


LOADER_MAP = {
    '.pdf': UnstructuredPDFLoader,
    '.ppt': UnstructuredPowerPointLoader,
    '.pptx': UnstructuredPowerPointLoader,
    '.doc': UnstructuredWordDocumentLoader,
    '.docx': UnstructuredWordDocumentLoader
}

def loadFile(filePath: str) -> BaseLoader:
    extension = splitext(filePath)[1]
    if extension not in LOADER_MAP.keys():
        return None
    loader = LOADER_MAP[extension]
    return loader(filePath)

def loadPath(dirPath: str) -> List[BaseLoader]:
    return [ loader for loader in [loadFile(f'{dirPath}/{f}') for f in listdir(dirPath)] if loader is not None]

def loadDocs(loaders: List[BaseLoader]):
    wrapperLists = [loader.load() for loader in loaders]
    return [doc for sublist in wrapperLists for doc in sublist]