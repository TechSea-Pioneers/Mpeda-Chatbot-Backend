import requests
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from llama_index.embeddings import LangchainEmbedding


def download_file(url, save_path):
    if not os.path.exists('Data'):
        os.makedirs('Data')
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to download the file: {response.status_code}')

def setup_memory(llm):
    documents = SimpleDirectoryReader("./Data").load_data()
    embed_model = LangchainEmbedding(
        HuggingFaceEmbeddings(model_name="thenlper/gte-large")
    )
    service_context = ServiceContext.from_defaults(
        chunk_size=256,
        llm=llm,
        embed_model=embed_model
    )
    index = VectorStoreIndex.from_documents(documents, service_context=service_context)
    return index.as_query_engine(), embed_model, service_context
